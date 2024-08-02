function [T] = approxder(f,a,N)
%provides a table of secant slope approximations
%to the derivative of f at a

%f = a symbolic function
%a = the point of interest
%N = the number of secant slopes to compute and display

xvalues = zeros(N,1);
%initializes the vector that will hold the x-values used for the
%second point defining each secant line


secslopes = zeros(N,1);
%initializes the vector that will hold the secant slopes 

for n = 1:N

    xvalues(n) = a+1/n;

end
%populates the vector of x-values

for n = 1:N
    secslopes(n) = double(vpa((f(xvalues(n))-f(a))/(xvalues(n)-a)));
end
%populates the vector of secant slopes

T = table(xvalues,secslopes,'VariableNames',{'x','(f(x) - f(a))/(x-a)'});
