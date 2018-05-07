
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

#define N 10000

int main()
{

    //FILE* fp = NULL;
    //fp = fopen("data.model", "w+");
    char str[100] = {};
    // char s[10] ={};
    char t = 0;
    int num = 0;
    // printf("hello");
    
    // char* *ele = malloc(N * 20 * sizeof(char) );
    // char* *x = malloc(N * 20 * sizeof(char) );
    // char* *y = malloc(N * 20 * sizeof(char) );
    // char* *z = malloc(N * 20 * sizeof(char) );
    char* ele[N] = {0};
    // char* x[N] = {0};
    // char* y[N] = {0};
    // char* z[N] = {0};
    // x[1] = "hi";
    // printf("%s",x[1]);
    for(int i = 0;i<N;i++)
    {
        ele[i]=malloc(10*sizeof(char));
        strcpy(ele[i], "X");
        // printf("%s", ele[i]);
        // x[i]=malloc(10*sizeof(char));
        // strcpy(x[i], "X");
        // y[i]=malloc(10*sizeof(char));
        // z[i]=malloc(10*sizeof(char));
    }
    // double e[N] = 0;
    srand( (unsigned int)time(0) );
    int ran = rand(); 
    double x[N] = {};
    double y[N] = {} ;
    double z[N] = {} ;
    for(int i = 0;i<N;i++)
    {
        x[i] = ran;
        y[i] = ran;
        z[i] = ran;        
    }
    double xlo,xhi,ylo,yhi,zlo,zhi = 0;
    
    // printf("hello");

    // scanf("%[^\n]", &t);
    // scanf("%[^\n]", &t);
    gets(str);  //REMARK
    gets(str);  //REMARK 

    gets(str);  //CRYST   read the crystal
    char* s = " ";
    char* temp = NULL;
    char* c = "CRYST1";
    temp = strtok(str, s);
    if( strcmp(temp, c)==0 )
    {
        xlo = 0;
        ylo = 0;
        zlo = 0;
        temp = strtok(NULL,s);
        xhi = atof(temp);
        temp = strtok(NULL, s);
        yhi = atof(temp);
        temp = strtok(NULL, s);
        zhi = atof(temp);
    }

    gets(str);  //ORI
    gets(str);
    gets(str);
    gets(str);  //SCALE
    gets(str);
    gets(str);


            // printf("!!!");


    // input the pdb data
    while(scanf("%c", &t))
    {
        // printf("%c", t);
        if(t == 'A')
        {
            // printf("%c",t);
            gets(str);
            char* p = " ";
            char* temp=NULL;
            // int t = atoi(str);

            temp =  strtok(str,p);  //tom
            temp =  strtok(NULL,p); //num
            num++;
            // printf("%d",num);
            temp =  strtok(NULL,p); //element
            int i = 0;
            char a = 0;
            while( temp[i] )
            {
                if( (temp[i] >= 'A') && ( temp[i] <= 'Z' ) )
                {
                    a = temp[i];
                    break;
                }
                i++;
            }
            // forchar a = temp[0] ;
            // strcpy(a,temp);
            strcpy(ele[num-1], &a );
            
            // printf("%s",ele[num-1]);
            
            temp =  strtok(NULL,p); //mol
            if( strcmp(temp, "MOL") != 0)
            {
                temp =  strtok(NULL,p); //mol
            }
            temp =  strtok(NULL,p); //mol num
            
            temp =  strtok(NULL,p); //x
            x[num-1] = atof(temp);
            // strcpy(x[num-1], temp);
            // printf("x %f", x[num-1]);
            temp =  strtok(NULL,p); //y
            // strcpy(y[num-1], temp);
            y[num-1] = atof(temp);
            // printf("y %f",y[num-1]);
            temp =  strtok(NULL,p); //z
            // strcpy(z[num-1], temp);
            z[num-1] = atof(temp);
            // printf("z %f\n",z[num-1]);
            
            // type[num] = 
            // printf("%d", num);
        }
        else if(t == 'R')
        {
            // scanf("%[^\n]", &t);
            gets(str);
            // printf("sno\n");
        }
        else if( (t=='C') || (t=='E')||(t=='T') )
        {
            // printf("over");
            break;
        }
    }

    // scanf("%d %[A-Z] %f %f %f %[\n] ", &num, &type, &x, &y, &z);

    // double xd[N] = {0};
    // double yd[N] = {0};
    // double zd[N] = {0};

    // int xyz(char* x[], char* y[], char* z[], double* xd,double* yd,double* zd)
    // {
    //     for(int i = 0;x[i]!=;i++)
    //     {
    //         xd[i] = atof(x[i]);
    //         // printf("%s\n",x[i]);
    //         yd[i] = atof(y[i]);
    //         // printf("%s",y[i]);
    //         // printf("%f\n",yd[i]);
    //         zd[i] = atof(z[i]);
    //     }
    //     return 0;
    // }
    
    // formxyz(x,y,z,xd,yd,zd);
    
    // the minimum and maximum of an array
    void minmax(double* m, double* lo, double* hi)
    {
        // int len = N;
        int i = 0;
        double temp = m[0];
        for(i = 0;m[i]!=ran;i++)
        {
            if(temp > m[i])
            {
                temp = m[i];
            }
        }
        *lo = temp-0.01;
                
        temp = m[0];
        for(i = 0;m[i]!=ran;i++)
        {
            if(temp < m[i])
            {
                temp = m[i];
            }
        }
        *hi = temp+0.01;        
    }
    if(xhi == 0)
    {
        minmax(x,&xlo,&xhi);
        // printf("%f", xlo);
        minmax(y,&ylo,&yhi);
        // printf("%f", ylo);
        minmax(z,&zlo,&zhi);
        // printf("%f", zlo);
    }
    // minmax(x,&xlo,&xhi);
    // // printf("%f", xlo);
    // minmax(y,&ylo,&yhi);
    // // printf("%f", ylo);
    // minmax(z,&zlo,&zhi);
    // // printf("%f", zlo);

    
    // the total number of tpyes
    // printf("hello");
    char* type[200] = {0};    
    for(int i=0;i<200;i++)
    {
        type[i]=malloc( 10 *sizeof(char)  );
        if(i==0) 
        {
            strcpy(type[i], "1");
            continue;
        }
        strcpy(type[i],"0");
    }
    int typecode[N] = {0};
    for(int m = 0; strcmp(ele[m],"X");m++)
    {
        // printf("hello");
        for(int n = 0;strcmp(type[n],"0");n++)
        {
            if (strcmp(ele[m],type[n])==0)
            {
                typecode[m]=n+1;
                // printf("%s",ele[m]);
                // printf("%d\n", typecode[m]);
                break;
            }
            else
            {
                if(strcmp(type[n],"1")==0)
                {
                    strcpy(type[n],ele[m]);
                    typecode[m]=n+1;
                }
                else if(strcmp(type[n+1],"0")==0)
                {
                    strcpy(type[n+1],ele[m]);
                }
            }
        }
    }
    int tn = 0;         //typenumber
    for(;type[tn]!=0;tn++){}

    double typemass(char* t)
    {
        if(strcmp(t,"C")==0)
        {
            return 12.0000;
        }
        else if(strcmp(t,"H")==0)
        {
            return 1.0080;
        }
        else if(strcmp(t,"O")==0)
        {
            return 15.9990;
        }
        else if(strcmp(t,"N")==0)
        {
            return 14.0000;
        }
        else if(strcmp(t,"S")==0)
        {
            return 32.0600;
        }
        
        // switch()
        // {
        //     case 'C':
        //     {
        //         return 12.0000;
        //         break;
        //     }
        //     case 'H':
        //     {
        //         return 1.0080;
        //         break;
        //     }
        //     case 'O':
        //     {
        //         return 15.9990;
        //         break;
        //     }
        //     case 'N':
        //     {
        //         return 14.0000;
        //         break;
        //     }
        //     case 'S':
        //     {
        //         return 32.0600;
        //         break;
        //     }
        // }
        
    }



    printf("# model data \n\n");
    // printf("\n")
    printf("%d atoms\n", num);
    
    int i = 0;
    for(;strcmp(type[i],"0");i++){}
    printf("%d atom types\n\n", i);

    printf("%f %f xlo xhi\n", xlo, xhi);
    printf("%f %f ylo yhi\n", ylo, yhi);
    printf("%f %f zlo zhi\n", zlo, zhi);
    printf("\nMasses\n\n");
    
    for(int d=0;strcmp(type[d],"0");d++)
    {
        printf("%d %f\n", (d+1), typemass(type[d]));
    }
    printf("\nAtoms\n\n");
    double e = 0.0;
    for(int l = 0;strcmp(ele[l],"X");l++)
    {
        printf("\t%d\t%d\t%f\t%f\t%f\t%f\n", (l+1), typecode[l], e, x[l], y[l], z[l]);
    }
    
    printf("\n");
    
    
    for(int i = 0;i<N;i++)
    {
        free(ele[i]);
        // free(x[i]);
        // free(y[i]);
        // free(z[i]);
    }
    for(int i =0;i<200;i++)
    {
        free(type[i]);
    }
    
    return 0;
}