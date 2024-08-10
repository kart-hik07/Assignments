clear
clc
close all


cd0 = 0.01686447;
%Condition
rho = 1.225;
Vinf = 20;
alpha = -1.25*(pi/180);
%Wing
h = 0.5; %taper ratio
bhalf = 0.7;
cr = 0.1; %root chord
clalpha = 5; %lift slope
part = 10;
z = 0;
for i=1:part
    theta(i) = (pi/2) - z*(pi/(2*part));
    y(i) = bhalf*cos(theta(i));
    ny(i) = bhalf/y(i);
    c(i) = 0.5; %rec
    %c(i) = cr*((1-h)*(bhalf-y(i))/(bhalf+h)); %taper wing
    %c(i) = cr*(1-((y(i)/bhalf)^2))^0.5; %elliptic wing
    vr(i) = Vinf;
    mu(i) = (clalpha*c(i)/(8*bhalf));
    %thetatwist(i) = 0; %no twist
    thetatwist(i) = -2/bhalf*y(i)*pi/180; %geometric twist
    %alphacl0(i) = -4*pi/180;
    alphacl0(i) = 0/bhalf*y(i)*pi/180;
    alphay(i) = thetatwist(i)+alpha;
    z = z+1;
end
for i=1:part-1
    dy(i) = y(i+1)-y(i);
end
dy(part) = 0;
n = 0;
for i=1:part
    for j=1:part
        a(i,j) = sin((2*n+1)*theta(i))*((2*n+1)*mu(i)+sin(theta(i)));
        n = n+1;
    end
    n=0;
end
area = 0;
for i=1:part
    area = area+c(i)*y(i);
end
for i=1:part
    b(i) = mu(i)*(alphay(i)-alphacl0(i))*sin(theta(i));
end
x = linsolve(a,b');
n=0;
xsum = 0;
for i=1:part
    for j=1:part
        xsum = xsum + 4*bhalf*vr(i)*x(j)*sin((2*n+1)*theta(i));
        n=n+1;
    end
    gamma(i) = xsum;
    lift(i) = gamma(i)*rho*vr(i);
    cl(i) = lift(i)/(0.5*rho*Vinf^2*c(i));
    xsum = 0;
    n = 0;
end
 xsum = 0;
 n = 0;
 for i=1:part
     for j=1:part
         xsum = xsum+(2*n+1)*x(j)*sin(theta(i)*(2*n+1))/sin(theta(i));
         n = n+1;
     end
     alphai(i) = xsum;
      xsum = 0;
      n = 0;
 end
 for i=1:part
     drag(i) = -lift(i)*sin(alphai(i))-0.5*rho*vr(i)^2*c(i)*dy(i)*cd0;
     wd(i) = vr(i)*sin(alphai(i)); %Downwash
 end
 cfv = 0;
 cft = 0;
 torq = 0;
 for i=1:part
     cfv = cfv + lift(i)*dy(i);
     cft = cft + drag(i)*dy(i);
 end
 Liftgrams = cfv*1000/9.8
 idraggrams = cft*1000/9.8
 LbyD = abs(cfv/cft);

 figure(1)
 plot(y,gamma)
 xlabel('span')
 ylabel('gamma')

 figure(2)
 plot(y,cl)
 xlabel('span')
 ylabel('cl/b')

 figure(3)
 plot(y,wd)
 xlabel('span')
 ylabel('downwash m/s')