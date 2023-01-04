#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf ("Usage: ./recover IMAGE \n");
        return 1;
    }
    FILE *f = fopen(argv[1], "r");
    if (f == NULL)
    {
        printf("File not found\n");
        return 1;
    }
    typedef uint8_t BYTE;
    BYTE buffer[512];
    char * filename = malloc(8 * sizeof(char));
    FILE * img;
    bool found = false;
    int counter = 0;
    while (fread(buffer,sizeof(BYTE),512,f))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (found)
                fclose(img);
            sprintf(filename, "%03i.jpg", counter);
            counter++;
            img = fopen(filename, "w");
            found = true;
        }
        if (found)
            fwrite(buffer,sizeof(BYTE),512,img);
    }
    fclose(f);
    fclose(img);
    free(filename);
}