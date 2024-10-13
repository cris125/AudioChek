import flet as ft

class State:
    toggle = True

s = State()

def main(page: ft.Page):
    # Datos desordenados
    data_points = [
        ft.LineChartDataPoint(x=10000, y=0.03), 
        ft.LineChartDataPoint(x=8000, y=0.03), 
        ft.LineChartDataPoint(x=12000, y=0.03),
        ft.LineChartDataPoint(x=16000, y=0.2),
        ft.LineChartDataPoint(x=19500, y=0.03), 
        ft.LineChartDataPoint(x=17000, y=0.4), 
        ft.LineChartDataPoint(x=18000, y=0.4), 
        ft.LineChartDataPoint(x=19000, y=1), 
        ft.LineChartDataPoint(x=20000, y=1)
    ]

    # Ordenar los puntos por el valor de x
    data_points_sorted = sorted(data_points, key=lambda point: point.x)

    # Crear el gráfico con los datos ordenados
    data = [
        ft.LineChartData(
            data_points=data_points_sorted,
            stroke_width=8,
            color=ft.colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
        )
    ]
    
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
        min_x=0,
        max_x=20000,
        expand=True,
    )

    page.add(chart)

ft.app(main)
