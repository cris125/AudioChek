import flet as ft
import json
class Results():
    def math_model(self):
        pass
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
                color=ft.colors.LIGHT_GREEN,
                curved=False,
                stroke_cap_round=True,),
                ft.LineChartData(
                data_points = points_ri_sorted,
                stroke_width=3,
                color=ft.colors.RED,
                curved=False,
                stroke_cap_round=True,)]
            
            
            chart = ft.LineChart(
                data_series=data,
                border=ft.Border(
                    bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
                ),
                left_axis=ft.ChartAxis(
                    
                    labels_size=40,
                ),
                bottom_axis=ft.ChartAxis(
                    
                    labels_size=32,
                ),

            min_y=0,
            max_y=1,
            min_x=7500,
            max_x=20000,
            # animate=5000,
            expand=True,
            )
            return (chart)
        else:
             
            res_test_smal=self.page.client_storage.get("res_test_small")
            data_x=[x[0] for x in res_test_smal]
            data_y=[1 if y[1]==None else  y[1] for y in res_test_smal]
            
            points=[ft.LineChartDataPoint(data_x[x],data_y[x]) for x in range(len(data_x))]
            data_points_sorted = sorted(points, key=lambda point: point.x)
            
            data=[ft.LineChartData(
                data_points = data_points_sorted,
                stroke_width=3,
                color=ft.colors.LIGHT_GREEN,
                curved=False,
                stroke_cap_round=True,)]
            
            chart = ft.LineChart(
                data_series=data,
                border=ft.Border(
                    bottom=ft.BorderSide(4, ft.colors.with_opacity(0.5, ft.colors.ON_SURFACE))
                ),
                left_axis=ft.ChartAxis(
                    
                    labels_size=40,
                ),
                bottom_axis=ft.ChartAxis(
                    
                    labels_size=32,
                ),

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
        colum=ft.Column([],expand=True)
        if self.page.client_storage.get("res_test_big") != None :
            
            colum.controls.append(
                ft.Container(content=self.char_data(1),
                             margin=10,padding=10))
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
                width=self.page.width/2.5,
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
            colum.controls.append(continer_big)
            
        if self.page.client_storage.get("res_test_small") != None:
            colum.controls.append(self.char_data(0))
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
                width=self.page.width/2.5,
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
            colum.controls.append(continer_small)
        return(colum)
            