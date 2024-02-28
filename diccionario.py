menu = dict({
    "pan_salado":{
        "articulo":list([
            {"nombre":"pan de avena","precio":2500},
            {"nombre":"pan de trigo","precio":2500},
            {"nombre":"pan de ajonjoli","precio":2500},
            {"nombre":"pan de 7 granos","precio":2500},
            {"nombre":"pan de redil","precio":2500},
            {"nombre":"pan de sal","precio":2500},
            {"nombre":"pan de uva pasa","precio":2500}
        ]),
        "promociones":list([
            {"codigo":0, "nombre": "por compras de 4","costo":9000},
            {"codigo":0, "nombre": "por compras de 5","costo":11500}        
        ])
    }
})
print("seleccione la categoria")
listacategoria = menu.keys()
listacategoria = list(listacategoria)
for i,val in enumerate(listacategoria):
    print(f"{1}.{val}")
    opcioncategoria = int(input())
    datoscategoria = menu.get(listacategoria[opcioncategoria])
    articuloscategoria = datoscategoria["articulo"]
    
    print(f"seeccione el aticulo de la categoria deseada {listacategoria[opcioncategoria]}")
    for i, val in enumerate(articuloscategoria):
        print(f"{i}.{val}")
    opcioncategoria = int(input())
    datoscategoria = menu.get(listacategoria[opcioncategoria])
    promocionesarticulo = datoscategoria.get("promociones")
    
    promocionesarticulo= list()
    for val in promocionesarticulo:
        if(val.get("codigo") == opcioncategoria):
            promocionesarticulo.append(val)
            if(len(promocionesarticulo)):
                
                if(len(promocionesarticulo) == 0):
                    print(f"promociones del articulo{datoscategoria.get('articulo')[opcioncategoria]}")
                else:
                    print(f"promociones del articulo{datoscategoria.get('articulo')[opcioncategoria]}"),
                    print(promocionesarticulo)
                    