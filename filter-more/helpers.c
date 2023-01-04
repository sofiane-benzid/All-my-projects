#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round(((float)image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        int a = 0;
        int b = width - 1;
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][a];
            image[i][a] = image[i][b];
            image[i][b] = temp;
            a++;
            b--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp [i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i ++)
    {
        for (int j = 0; j < width; j++)
        {
            int counter = 0;
            int red, green, blue;
            red = green = blue = 0;
            for (int a = -1; a <= 1; a++)
            {
                for (int b = -1; b <= 1; b++)
                {
                    if (i + a > height - 1 || i + a < 0 || j + b > width - 1 || j + b < 0)
                        continue;
                    counter++;
                    red += image[i + a][j + b].rgbtRed;
                    green += image[i + a][j + b].rgbtGreen;
                    blue += image[i + a][j + b].rgbtBlue;
                }
            }
            temp[i][j].rgbtRed = round((float)red/counter);
            temp[i][j].rgbtGreen = round((float)green/counter);
            temp[i][j].rgbtBlue = round((float)blue/counter);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    int Gx[3][3] = {{-1, 0 , 1}, {-2, 0 , 2}, {-1, 0 , 1}};
    int Gy[3][3] = {{-1, -2 , -1}, {0, 0, 0}, {1, 2, 1}};
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redx, greenx, bluex;
            redx = greenx = bluex = 0;
            int redy, greeny, bluey;
            redy = greeny = bluey = 0;
            int red, green, blue;
            red = green = blue = 0;
            for (int a = -1; a <= 1; a++)
            {
                for (int b = -1; b <= 1; b++)
                {
                    if (i + a > height - 1 || i + a < 0 || j + b > width - 1 || j + b < 0)
                    {
                        continue;
                    }
                    redx += image[i + a][j + b].rgbtRed * Gx[a + 1][b + 1];
                    redy += image[i + a][j + b].rgbtRed * Gy[a + 1][b + 1];
                    greenx += image[i + a][j + b].rgbtGreen * Gx[a + 1][b + 1];
                    greeny += image[i + a][j + b].rgbtGreen * Gy[a + 1][b + 1];
                    bluex += image[i + a][j + b].rgbtBlue * Gx[a + 1][b + 1];
                    bluey += image[i + a][j + b].rgbtBlue * Gy[a + 1][b + 1];
                }
            }
            red = round((float)sqrt((redx*redx)+(redy*redy)));
            green = round((float)sqrt((greenx*greenx)+(greeny*greeny)));
            blue = round((float)sqrt((bluex*bluex)+(bluey*bluey)));
            if (red > 255)
                red = 255;
            if (green > 255)
                green = 255;
            if (blue > 255)
                blue = 255;
            temp[i][j].rgbtRed = red;
            temp[i][j].rgbtGreen = green;
            temp[i][j].rgbtBlue = blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}
