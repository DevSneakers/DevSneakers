%% 신호 생성
clc; clear; close all;
[a_t,fm] = audioread('SAMPLE_2.mp3');
b_t=a_t(1:1*fm,1);
b_t2=a_t(1:1*fm,2);

dt1=1/fm;
t1=0:dt1:(dt1*length(b_t))-dt1;

OSR=10; %업샘플율
fs = fm*OSR;

dt2 = dt1/OSR; % = 1/fs
t2 = 0:dt2:(dt1*length(b_t))-dt2;
m_t1=interp1(t1,b_t,t2);
m_t2=interp1(t1,b_t2,t2);
a1 = 1.0;
Ac=10;
fc = 1*10^6;
c_t = Ac*cos(2*pi*fc*t2);
mn_t1 = m_t1/abs(min(m_t1));
mn_t2 = m_t2/abs(min(m_t2));



for snr_dB = -20 : 1 : 20   % linear 스케일
                % dB스케일로 구현될 수 있음 -> 10 dB환경
    snr = db2pow(snr_dB); % dB스케일 -> linear스케일 변환
   
        % 신호 생성
         x_t1 = (1+(a1*mn_t1)).*c_t;
         x_t2 = (1+(a1*mn_t2)).*c_t;
        % 채널 생성 (SISO환경)
        h1 = randn(1, 1);% randn : 평균이 0이고 분산이 1인 정규분포를 따르는 랜덤 숫자 발생
        h2 = randn(1, 1);                 % n1 X n2 행렬 발생

        % 노이즈 생성 (SISO환경)
        Ps1 = sum(abs(x_t1).^2)/length(x_t1);
        Pn1 = Ps1 / snr;
        
        Ps2 = sum(abs(x_t2).^2)/length(x_t2);
        Pn2 = Ps2 / snr;
        
        n1= sqrt(Pn1) * randn(1,length(x_t1));
        n2= sqrt(Pn2) * randn(1,length(x_t2));
end
figure(1);
subplot(2, 1, 1);
plot(t2, x_t1);
subplot(2, 1, 2);
plot(t2, (4*h1) * x_t1);

% 수신 신호 생성
y_t_1 = (4*h1) * x_t1 + n1;
y_t_2 = h2 * x_t2 + n2;

figure(2);
subplot(2, 1, 1);
plot(t2, (4*h1) * x_t1);
subplot(2, 1, 2);
plot(t2,y_t_1);

figure(3);
subplot(2, 1, 1);
plot(t2,y_t_1);
subplot(2, 1, 2);
plot(t2, y_t_1/(4*h1));


%이퀄라이저 (Equalizer)

x_hat1 = y_t_1/h1;
x_hat2 = y_t_2/h2;

xr_t1 = sqrt(x_hat1 .* x_hat1);
d_t1 = lowpass(xr_t1, 1.7*10^4, fs);
yd_t1 = (((sqrt(2)/Ac)*abs(d_t1)-1)/a1)*abs(min(m_t1));