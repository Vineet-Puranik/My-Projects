function [dat] = eulers(F,t0,y0,tf,N)

dt=(tf-t0)/N;
y=zeros(N+1,1);
y(1)=y0;
t = zeros(N+1,1);

for n = 1:N+1
    t(n) = t0 + (n-1)*dt;
end

for n = 1:N
    y(n+1) = y(n) + F(t(n),y(n))*dt;
end

dat=table(t,y,'VariableNames',{'t','y'});






