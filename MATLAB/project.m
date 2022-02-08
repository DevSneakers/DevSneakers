%% project.m
clc; clear; close all;

%메세지 신호 생성
[a_t,fm] = audioread('SAMPLE_2.mp3');
b_t=a_t(1:end,1);
b_t2=a_t(1:end,2);

dt1=1/fm;
t1=0:dt1:dt1*(length(b_t)-1);

figure(1);
subplot(2, 1, 1);
plot(t1,b_t);%업샘플링 전 신호 플롯
axis([5 5.0025 -1 1])
subplot(2, 1, 2);
plot(t1,b_t2);

OSR=10; %업샘플율

dt2=dt1/OSR;
t2=0:dt2:dt1*(length(b_t)-1);

m_t1=interp1(t1,b_t,t2);
m_t2=interp1(t1,b_t2,t2);

figure(2);
subplot(2, 1, 1);
plot(t2,m_t1);
axis([5 5.0025 -1 1])
%업생픔링 후 신호 플롯 ( 한 프레임 안에 넣기)
% 크기 확인은 cmd 창에 size로 확인한다. size(a_t) 
subplot(2, 1, 2);
plot(t2, m_t2);

fs=fm*10;
BW= fs/2;
f=linspace(-BW,BW,length(t2));
m_f1 = fft(m_t1);
M_f1 = fftshift(m_f1);
M_f_mag1 = abs(M_f1);

m_f2 = fft(m_t2);
M_f2 = fftshift(m_f2);
M_f_mag2 = abs(M_f2);

figure(3);
subplot(2, 1, 1);
plot(f, M_f_mag1);
subplot(2, 1, 2);
plot(f, M_f_mag2);

%변조 신호 생성(DSB-LC)
a1 = 1.0;
Ac=100;
fc = 1*10^5;
c_t = Ac*cos(2*pi*fc*t2);
mn_t1 = m_t1/abs(min(m_t1));
mn_t2 = m_t2/abs(min(m_t2));
x_t1 = (1+(a1*mn_t1)).*c_t;
x_t2 = (1+(a1*mn_t2)).*c_t;

x_f1 = fft(x_t1);
X_f1 = fftshift(x_f1);
X_f_mag1 = abs(X_f1);

figure(4);
subplot(2, 1, 1);
plot(t2, x_t1);
subplot(2, 1, 2);
plot(f, X_f_mag1);

xr_t1 = sqrt(x_t1 .* x_t1);
d_t1 = lowpass(xr_t1, 5*10^4, fs);
yd_t1 = (((sqrt(2)/Ac)*abs(d_t1)-1)/a1)*abs(min(m_t1));

figure(5);
subplot(2, 1, 1);
plot(t2, yd_t1);
subplot(2, 1, 2);
plot(t2, yd_t1);
axis([5 5.0025 -1 1])

figure(6);
plot(t1, b_t); hold on;
plot(t2, m_t1);
plot(t2, yd_t1);
legend('원신호', '오버샘플링', '복조신호');
axis([5 5.0025 -1 1])

xr_t2 = sqrt(x_t2 .* x_t2);
d_t2 = lowpass(xr_t2, 5*10^4, fs);
yd_t2 = (((sqrt(2)/Ac)*abs(d_t2)-1)/a1)*abs(min(m_t2));

figure(7);
plot(t1, b_t2); hold on;
plot(t2, m_t2);
plot(t2, yd_t2);
legend('원신호', '오버샘플링', '복조신호');
axis([5 5.0025 -1 1])

x_t_1(1,:);
x_t_2(2,:);

%X_f = fft(x_t1)/dt;
%X_f = fftshift(X_f);
%X_f_mag=abs(X_f); %주파수 진폭 스펙트럼

% 복조신호 y_D(t) 형성하여 m(t)와 비교 -잘 되었는지

%랜덤채널 h 생성 / AWGN 잡음 n 생성

h1=randn;
h2=randn;
n1=randn(1,2);
n2=randn(1,2);

y_1= (h1*x_t_1)+n1;
figure(3);
%SISO
plot(t2,y_1);
y_2= (h2*x_t_2)+n2;
figure(4);