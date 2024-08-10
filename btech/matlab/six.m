l1=5;
l2=6;
Theta1=0;
Theta2=0;

x1=l1*cosd(Theta1);
y1=l1*sind(Theta1);
x2=l1*cosd(Theta1)+ l2*cosd(Theta1+Theta2);
y2=l1*sind(Theta1)+ l2*sind(Theta1+Theta2);

axis([-15 15 -15 15]);
grid on;
hold off;
while true
Q=[Theta1;Theta2];
ss=0;
figure(1)
[xt,yt]=ginput(1);

plot([0 x1],[0 y1], 'b', 'linewidth',4); hold on; plot(xt,yt, '*r');
plot([x1 x2],[y1 y2], 'r', 'linewidth',4); hold on;

while (ss==0)
    dxdtht1=-l1*sind(Q(1))-l2*sind(Q(1)+Q(2));
    dxdtht2=-l2*sind(Q(1)+Q(2));
    dydtht1=l1*cosd(Q(1))+l2*cos(Q(1)+Q(2));
    dydtht2=l2*cosd(Q(1)+Q(2));
    J=[dxdtht1, dxdtht2, dydtht1, dydtht2,]
    
    dx=[xt-x2;yt-y2];
    dq=(J')*dx
    Q=Q+0.2*dq
    x1=l1*cosd(Q(1));
    y1=l1*sind(Q(1));
x2=l1*cosd(Q(1))+ l2*cosd(Q(1)+Q(2));
y2=l1*sind(Q(1))+ l2*sind(Q(1)+Q(2));
plot([0,x1],[0,y1], 'r', 'linewidth', 4);
hold on;
plot(xt,yt, '*r');
plot([x1,x2],[y1,y2],'b', 'linewidth', 4);
axis([-15 15 -15 15]);
grid on;
dis=sqrt((xt-x2)^2 + (yt-y2)^2);
hold off;
if (dis<0.1)
ss=1;
pause(1.0)
end
end
end
