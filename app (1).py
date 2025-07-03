
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dummy-Daten simulieren (wie im Original)
np.random.seed(42)
data = pd.DataFrame({
    'Vorvertragliche nachhaltige Mindestinvestitionen (in %)': np.random.randint(1, 101, 50)
})

column = 'Vorvertragliche nachhaltige Mindestinvestitionen (in %)'

st.title("Analyse der vorvertraglichen Mindestinvestitionen")

# Eingabemaske
user_value = st.number_input("Bitte gib deinen Wert ein (in %):", min_value=0, max_value=150, value=50)

if st.button("Analyse starten"):
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
        f'Input-Wert: {user_value} %',
        f'Anzahl Werte: {num_values}',
        f'Mittelwert: {mean_val:.1f} %',
        f'Median: {median_val:.1f} %',
        f'{percentile:.1f}% der Werte sind kleiner als {user_value} %'
    ))
    props = dict(boxstyle='round', facecolor='white', alpha=0.8)
    ax.text(0.70, 0.95, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

    # Linien im Hauptplot
    ax.axvline(user_value, color='red', linestyle='--', linewidth=2, label='Input-Wert')
    ax.axvline(mean_val, color='green', linestyle=':', linewidth=2, label='Mittelwert')
    ax.axvline(median_val, color='blue', linestyle='-.', linewidth=2, label='Median')

    ax.set_title('Analyse: Vorvertragliche nachhaltige Mindestinvestitionen (in %)')
    ax.set_xlabel('Wert (%)')
    ax.set_ylabel('Häufigkeit')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
