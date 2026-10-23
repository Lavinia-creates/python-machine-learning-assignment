from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Each row contains monthly spending (KES) and monthly shopping visits.
customers = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4],
]

# Scale both measurements so spending's larger numbers do not dominate clustering.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(customers)

# Fit three clusters, then assign each customer to its nearest cluster.
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X_scaled)
clusters = model.predict(X_scaled)

for customer_number, cluster in enumerate(clusters, start=1):
    print(f"Customer {customer_number} belongs to Cluster {cluster}")

# Count how many customers were assigned to each cluster.
cluster_counts = {cluster_number: 0 for cluster_number in range(3)}
for cluster in clusters:
    cluster_counts[cluster] += 1

print("\nTotal customers in each cluster:")
for cluster_number, count in cluster_counts.items():
    print(f"Cluster {cluster_number}: {count} customers")

# Bonus: show customers coloured by their K-Means group.
scatter = plt.scatter(
    [customer[0] for customer in customers],
    [customer[1] for customer in customers],
    c=clusters,
    cmap="viridis",
    s=80,
)
plt.xlabel("Monthly spending (KES)")
plt.ylabel("Monthly visits")
plt.title("Customer groups from K-Means")
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
plt.show()
