def knapsack_dp(weights, values, capacity):
    n = len(weights)

    # Membuat tabel DP (n+1) x (capacity+1) dan isi awal = 0
    DP = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # --- Fase 1: Mengisi tabel DP ---
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # Berat barang ke-i
            wi = weights[i - 1]
            vi = values[i - 1]

            # Jika barang tidak muat
            if wi > w:
                DP[i][w] = DP[i - 1][w]
            else:
                # Bandingkan: tidak ambil barang vs ambil barang
                DP[i][w] = max(
                    DP[i - 1][w],                 # tidak diambil
                    DP[i - 1][w - wi] + vi        # diambil
                )

    # --- Fase 2: Rekonstruksi barang yang terpilih ---
    chosen_items = []
    w = capacity

    for i in range(n, 0, -1):
        # Jika nilai berubah dari baris atas → barang ini diambil
        if DP[i][w] != DP[i - 1][w]:
            chosen_items.append(i - 1)
            w -= weights[i - 1]

    chosen_items.reverse()  # agar tampil berurutan

    return DP[n][capacity], chosen_items, DP
# Contoh penggunaan fungsi
weights = [10, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
max_value, items, dp_table = knapsack_dp(weights, values, capacity)
print("Nilai maksimum yang dapat dicapai:", max_value)
print("Barang yang dipilih (indeks):", items+1)
