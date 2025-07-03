
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Daten einlesen (in Realität aus Datei)
np.random.seed(42)
num_rows = 50
isin_list = [f"DE{np.random.randint(1000000000, 9999999999)}" for _ in range(num_rows)]
data = pd.DataFrame({
    'ISIN': isin_list,
    'Vorvertragliche nachhaltige Mindestinvestitionen (in %)': np.random.randint(1, 101, num_rows)
})

column = 'Vorvertragliche nachhaltige Mindestinvestitionen (in %)'

st.title("Analyse EET Daten")

# Eingabemaske
user_isin = st.text_input("Bitte gib die ISIN ein:").strip().upper()

if st.button("Analyse starten"):
    if user_isin not in data['ISIN'].values:
        st.error("ISIN nicht gefunden. Bitte überprüfe deine Eingabe.")
    else:
        user_value = data.loc[data['ISIN'] == user_isin, column].values[0]

        # Statistik
        mean_val = data[column].mean()
        median_val = data[column].median()
        percentile = (data[column] < user_value).mean() * 100
        num_values = data[column].count()

        # Plot erstellen
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(data[column], bins=10, edgecolor='black', alpha=0.3, label='Verteilung')

        # Zusatzachsen für Boxplot
        box_ax = fig.add_axes([0.15, 0.15, 0.7, 0.1])
        box_ax.boxplot(data[column], vert=False, patch_artist=True)
        box_ax.axvline(user_value, color='red', linestyle='--', linewidth=2)
        box_ax.set_yticks([])
        box_ax.set_xlabel('')
        box_ax.set_title('Boxplot')

        # Zusatzinfos
        textstr = '\n'.join((
            f'ISIN: {user_isin}',
            f'Wert: {user_value} %',
            f'Anzahl Werte: {num_values}',
            f'Mittelwert: {mean_val:.1f} %',
            f'Median: {median_val:.1f} %',
            f'{percentile:.1f}% der Werte sind kleiner als {user_value} %'
        ))
        props = dict(boxstyle='round', facecolor='white', alpha=0.8)
        ax.text(0.70, 0.95, textstr, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', bbox=props)

        # Linien im Hauptplot
        ax.axvline(user_value, color='red', linestyle='--', linewidth=2, label='Wert zur ISIN')
        ax.axvline(mean_val, color='green', linestyle=':', linewidth=2, label='Mittelwert')
        ax.axvline(median_val, color='blue', linestyle='-.', linewidth=2, label='Median')

        ax.set_title('Analyse: Vorvertragliche nachhaltige Mindestinvestitionen (in %)')
        ax.set_xlabel('Wert (%)')
        ax.set_ylabel('Häufigkeit')
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)
