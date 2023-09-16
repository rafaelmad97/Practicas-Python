def generarBandera(sizey,sizex):
    x = 0 
    y = 0
    bandera = ""
    midx = sizex//2
    midy = sizey//2
    while x < sizex and y < sizey:
        if x == midx or y == midy: 
            bandera += " + "
        else:
            bandera += " 0 "
        x+=+1
        if x == sizex:
            bandera += "\n"
            x=0
            y+=+1
    return bandera

def main():
    size_x = size_y = 0
    x = y = False 
    while size_x % 2 == 0 or size_y % 2 == 0:
        if x == False :
            print("Ingrese el x tamaño de la bandera")
            size_x = int(input())
        if y == False:
            print("Ingrese el y tamaño de la bandera")
            size_y = int(input())
        
        y = size_y % 2 != 0 and size_y < 200 and size_y > 0
        
        x = size_x % 2 != 0 and size_x < 200 and size_x > 0

        if x and y:
            break
        else:
            print("el valor debe ser impar, no debe exceder a 200 y debe ser mayor a cero")
    print("\n")
    print(f"x={size_x} y={size_y}\n")

    print(generarBandera(size_y,size_x))

main()