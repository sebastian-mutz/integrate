program e001
    implicit none

    real, parameter :: radius = 2.0
    real, parameter :: pi = 3.141592653589793
    real :: circumference
    real :: area

    circumference = 2.0 * pi * radius
    area = pi * radius ** 2

    print *, "circumference =", circumference
    print *, "area =", area
end program e001
