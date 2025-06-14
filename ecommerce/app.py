import conn_duckdb as cd
import streamlit as st


def sales_per_month():
    conn = cd.get_conn()
    st.title('Total sales per month')
    month_sale = """
    SELECT
        MonthSale
        , SUM(Total) AS Total
    FROM
        SALES
    GROUP BY
        MonthSale
    ORDER BY
        MonthSale
    """
    df_db = conn.execute(month_sale).fetchdf()
    st.bar_chart(data=df_db.set_index('MonthSale')['Total'])


def sales_per_month_country():
    conn = cd.get_conn()
    st.title('Total sales per month by country')
    list_countries = """
        SELECT DISTINCT
            Country
        FROM
            SALES
        ORDER BY
            Country
    """
    df_countries = conn.execute(list_countries).fetch_df()
    countries = df_countries['Country'].to_list()
    country_select = st.selectbox('Choose country', countries)
    country_sales = f"""
        SELECT
            MonthSale
            , SUM(Total) AS Total
        FROM
            sales
        WHERE
            Country = '{country_select}'
        GROUP BY
            MonthSale
        ORDER BY
            MonthSale
    """
    df_db = conn.execute(country_sales).fetchdf()
    st.bar_chart(data=df_db.set_index('MonthSale')['Total'])


def top_itens_per_month():
    conn = cd.get_conn()
    st.title('Top sold itens per month')
    list_months = """
        SELECT DISTINCT
            MonthSale
        FROM
            SALES
        ORDER BY
            MonthSale
    """
    df_months = conn.execute(list_months).fetch_df()
    months = df_months['MonthSale'].to_list()
    month_select = st.selectbox('Choose month', months)
    month_sales = f"""
        SELECT
            Description
            , SUM(Quantity) AS Products_Sold
            , ROUND(AVG(UnitPrice), 2) AS Average_Price
            , SUM(Total) AS Revenue
        FROM
            sales
        WHERE
            MonthSale = '{month_select}'
        GROUP BY
            Description
        ORDER BY
            Products_Sold DESC
        LIMIT 10
    """
    df_db = conn.execute(month_sales).fetchdf()
    st.dataframe(df_db, use_container_width=True)


if __name__ == '__main__':
    sales_per_month()
    sales_per_month_country()
    top_itens_per_month()
