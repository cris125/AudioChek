import flet as ft
import json
from  datetime import datetime
class Results():
    def edad(self):
        fecha_nacimiento =self.page.client_storage.get("date")
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        fecha_actual = datetime.now()
        edad = fecha_actual.year - fecha_nacimiento.year
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
            edad -= 1
        return(edad)
    def maxFrec(self,data_test:list):
        if len(data_test) > 0:
            frec=[x for x in data_test]
            return min(frec)
        else:
            return(20761)
    def math_model(self):
        def model(hz_max):
            
            fun= (-165.8*self.edad())+20761
            hzPer=(hz_max*100)/fun
            if hzPer>100:
                hzPer=100
            if hzPer<0:
                hzPer=0
            return(int(hzPer))
        
        small=None  
        big_r=None 
        big_l=None   
        
        res_test_smal=self.page.client_storage.get("res_test_small")
        res_test_big=self.page.client_storage.get("res_test_big")
        
        if res_test_smal:
            res_test_smal=[x[0] for x in res_test_smal if x[1] == None]
            max_f=self.maxFrec(res_test_smal)
            small=model(max_f)
            
        if res_test_big:
            dat_l=[dat[0] for dat in res_test_big if dat[2] == -1 and dat[1] == None  ]
            dat_r=[dat[0] for dat in res_test_big if dat[2] == 1 and dat[1] == None ]
            max_f_r=self.maxFrec(dat_r)
            max_f_l=self.maxFrec(dat_l)
            big_r=model(max_f_r)
            big_l=model(max_f_l)
                        
        return ({"small":small,
                 "big_r":big_r,
                 "big_l":big_l
                 })
    def msg_es(self,porc):
        if porc >=80:
            return(ft.colors.GREEN,"Audicion Normal")
        elif porc < 80 and porc > 55:
            return(ft.colors.ORANGE,"Perdida audicion moderada")
        elif porc < 55:
            return(ft.colors.RED,"Perdida audicion grave")
        
    def char_data(self,test):
        if test == 1:
            res_test_big=self.page.client_storage.get("res_test_big")
            dat_r=[dat for dat in res_test_big if dat[2] == 1 ]
            dat_l=[dat for dat in res_test_big if dat[2] == -1 ]
            
            data_x_r=[x[0] for x in dat_r]
            data_y_r=[1 if y[1]==None else  y[1] for y in dat_r]
            
            data_x_l=[x[0] for x in dat_l]
            data_y_l=[1 if y[1]==None else  y[1] for y in dat_l]
            
            points_r=[ft.LineChartDataPoint(data_x_r[x],data_y_r[x]) for x in range(len(data_y_r))]
            points_ri_sorted = sorted(points_r, key=lambda point: point.x)
            
            points_l=[ft.LineChartDataPoint(data_x_l[x],data_y_l[x]) for x in range(len(data_y_l))]
            points_le_sorted = sorted(points_l, key=lambda point: point.x)
            
            data=[
                ft.LineChartData(
                    data_points = points_le_sorted,
                    stroke_width=3,
                    color=ft.colors.RED,
                    curved=False,
                    stroke_cap_round=True,),
                ft.LineChartData(
                    data_points = points_ri_sorted,
                    stroke_width=3,
                    color=ft.colors.BLUE,
                    curved=False,
                    stroke_cap_round=True,)]
        else:
             
            res_test_smal=self.page.client_storage.get("res_test_small")
            data_x=[x[0] for x in res_test_smal]
            data_y=[1 if y[1]==None else  y[1] for y in res_test_smal]
            
            points=[ft.LineChartDataPoint(data_x[x],data_y[x]) for x in range(len(data_x))]
            data_points_sorted = sorted(points, key=lambda point: point.x)
            
            data=[ft.LineChartData(
                data_points = data_points_sorted,
                stroke_width=3,
                color=ft.colors.BLUE,
                curved=False,
                stroke_cap_round=True,)]
            
        chart = ft.LineChart(
                data_series=data,
                border=ft.Border(
                    bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
                ),
                left_axis=ft.ChartAxis(labels=[
                    ft.ChartAxisLabel(value=0,label=ft.Text("vol 0%", size=13, weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=0.5,label=ft.Text("vol 50%", size=13, weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=1,label=ft.Text("vol 100%", size=10, weight=ft.FontWeight.BOLD))
                    ,],labels_size=50),

                bottom_axis=ft.ChartAxis(labels=[
                    ft.ChartAxisLabel(value=8000,label=ft.Text("8khz", size=15, weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=10000,label=ft.Text("10khz", size=14, weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=15000,label=ft.Text("15khz", size=14, weight=ft.FontWeight.BOLD)),
                    ft.ChartAxisLabel(value=20000,label=ft.Text("20khz", size=14, weight=ft.FontWeight.BOLD))
                    ,],labels_size=50),

            min_y=0,
            max_y=1,
            min_x=7500,
            max_x=20000,
            # animate=5000,
            expand=True,
            )
        return (chart)
    def results(self,page:ft.Page):
        self.page=page
        tes_sm=ft.Row([],width=self.page.width)
        tes_big=ft.Row([],width=self.page.width)
        mat_model=self.math_model()
        if self.page.client_storage.get("res_test_big") != None :
            big_r=mat_model['big_r']
            big_l=mat_model['big_l']
            tes_big.controls.append(
                ft.Container(content=ft.Column([
                            ft.Row([ft.Text(value=f"Prueba larga",style=ft.TextThemeStyle.TITLE_MEDIUM,weight=ft.FontWeight.BOLD),
                                    ],alignment=ft.alignment.center),  
                            self.char_data(1),
                            ft.Row([ft.Text(value=f"Derecha %{big_r}",weight=ft.FontWeight.BOLD),
                                    ft.Text(value=self.msg_es(big_r)[1],color=self.msg_es(big_r)[0],weight=ft.FontWeight.BOLD),
                                    ft.Icon(name=ft.icons.AREA_CHART_SHARP,color=ft.colors.BLUE)]
                                    ,alignment=ft.alignment.center)  ,
                            ft.Row([
                                    ft.Text(value=f"Izquierda %{big_l} ",weight=ft.FontWeight.BOLD),
                                    ft.Text(value=self.msg_es(big_r)[1],color=self.msg_es(big_r)[0],weight=ft.FontWeight.BOLD),
                                    ft.Icon(name=ft.icons.AREA_CHART_SHARP,color=ft.colors.RED)]
                                    ,alignment=ft.alignment.center)                  
                            ],alignment=ft.MainAxisAlignment.CENTER,
                            ),
                             margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                padding=5,
                expand=True, adaptive=True,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                
                ))
        else:
            continer_big=ft.Container(
                 content=ft.Column([
                    ft.Text(value="Sin datos PRUEBA LARGA",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NO_CELL ,size=30),
                    ft.Text(value="Haz la prueba larga",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.BLACK),
                 ]),
                margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                width=self.page.width,
                expand=True,adaptive=True,
                padding=20,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                
            )
            tes_big.controls.append(continer_big)
            
        if self.page.client_storage.get("res_test_small") != None:
            small=int(mat_model["small"])
            tes_sm.controls.append(
                ft.Container(
                    content=
                    ft.Column([
                            ft.Row([ft.Text(value=f"Prueba corta",style=ft.TextThemeStyle.TITLE_MEDIUM,weight=ft.FontWeight.BOLD),
                                    ],alignment=ft.alignment.center),
                            self.char_data(0),
                            ft.Row([ft.Text(value=f"Nivel audicion %{small}",weight=ft.FontWeight.BOLD),
                                    ft.Text(value=self.msg_es(small)[1],color=self.msg_es(small)[0],weight=ft.FontWeight.BOLD),
                                    ft.Icon(name=ft.icons.AREA_CHART_SHARP,color=ft.colors.BLUE)
                                    ],alignment=ft.alignment.center),
                                    
                            ],alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                expand=True,
                
                padding=5,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                shadow=ft.BoxShadow(  # Añadir sombra suave
                    spread_radius=2,
                    blur_radius=15,
                    color=ft.colors.BLUE_GREY_400,
                    offset=ft.Offset(5, 5)
                ))
                                  )
            
            
            
        else:
            continer_small=ft.Container(
                 content=ft.Column([
                    ft.Text(value="Sin datos PRUEBA CORTA",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.BLACK),
                    ft.Icon(name=ft.icons.NO_CELL ,size=30),
                    ft.Text(value="Haz la prueba corta",style=ft.TextThemeStyle.LABEL_MEDIUM, 
                            color=ft.colors.BLACK),
                 ],horizontal_alignment=ft.MainAxisAlignment.CENTER),
                margin=10,
                bgcolor=ft.colors.LIGHT_BLUE_50,  # Fondo azul claro
                width=self.page.width,
                expand=True,
                padding=20,
                border_radius=20,  # Bordes más redondeados
                border=ft.border.all(2, ft.colors.BLUE_GREY_300),  # Bordes gris claro
                shadow=ft.BoxShadow(  # Añadir sombra suave
                    spread_radius=2,
                    blur_radius=15,
                    color=ft.colors.BLUE_GREY_400,
                    offset=ft.Offset(5, 5)
                )
            )
            tes_sm.controls.append(continer_small)
        return(ft.Column([tes_big,tes_sm],scroll=True))
            