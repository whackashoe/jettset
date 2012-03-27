int iterations = 2000;
double magic   = 2000.0;
double scaleX  = 10000.0;
double scaleY  = 100.0;
double offsetX = 3500000.0;
double offsetY = 30000.0;

int jett(double a, double b, double c) {
    for (int i=0; i<iterations; i++) {
        double d = a/b //new bottom number
        double e = c+d //new top number

        a = b //move b to the left
        b = e //add new b
        c = d //add new c
        if (a == 2.0 && b == 2.0 && a == 1.0) return i; //infinite sequence for scope
    }

    return -1;
}
