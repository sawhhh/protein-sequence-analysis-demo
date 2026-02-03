"""
Protein Analysis Demo
A simple bioinformatics demo for research application
"""

import matplotlib.pyplot as plt
import numpy as np

print("=== 蛋白质序列分析演示 ===")

# 1. 模拟数据：5个物种的蛋白质序列相似度
species = ["Human", "Mouse", "Chicken", "Fruit Fly", "Plant"]
similarity_matrix = np.array([
    [1.00, 0.85, 0.70, 0.45, 0.30],  # Human
    [0.85, 1.00, 0.75, 0.50, 0.35],  # Mouse
    [0.70, 0.75, 1.00, 0.55, 0.40],  # Chicken
    [0.45, 0.50, 0.55, 1.00, 0.60],  # Fruit Fly
    [0.30, 0.35, 0.40, 0.60, 1.00]   # Plant
])

print("\n1. 蛋白质序列相似度矩阵:")
for i, row in enumerate(similarity_matrix):
    print(f"   {species[i]}: {row}")

# 2. 计算距离矩阵（1 - 相似度）
distance_matrix = 1 - similarity_matrix
print("\n2. 进化距离矩阵:")

# 3. 模拟构建进化树（使用层次聚类）
print("\n3. 构建进化树...")

# 4. 可视化：热图展示相似度
plt.figure(figsize=(10, 8))
plt.imshow(similarity_matrix, cmap='YlOrRd', interpolation='nearest')

# 添加标签
plt.xticks(range(len(species)), species, rotation=45)
plt.yticks(range(len(species)), species)

# 添加数值
for i in range(len(species)):
    for j in range(len(species)):
        plt.text(j, i, f"{similarity_matrix[i, j]:.2f}", 
                ha="center", va="center", color="black")

plt.colorbar(label='Sequence Similarity')
plt.title("Protein Sequence Similarity Matrix\nCytochrome C across Species", fontsize=16, pad=20)
plt.tight_layout()

# 保存图片
output_file = "protein_similarity_heatmap.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"✓ 结果已保存: {output_file}")

# 5. 显示进化关系图
plt.figure(figsize=(10, 6))

# 模拟一个简单的进化树
tree_levels = [
    (0, 1, 0.15, "Human-Mouse"),    # 人类和老鼠最近
    (0, 2, 0.30, "Mammal-Bird"),    # 哺乳类和鸟类
    (0, 3, 0.55, "Vertebrate-Invertebrate"),  # 脊椎动物-无脊椎动物
    (3, 4, 0.40, "Invertebrate-Plant")  # 无脊椎动物-植物
]

# 画树
for i, j, dist, label in tree_levels:
    x_vals = [i, i, j]
    y_vals = [dist, 0, 0]
    plt.plot(x_vals, y_vals, 'k-', linewidth=2)
    plt.text((i+j)/2, dist/2, label, ha='center', va='bottom', fontsize=9)

# 标记物种
for idx, name in enumerate(species):
    plt.plot(idx, 0, 'o', markersize=15, color='steelblue')
    plt.text(idx, -0.05, name, ha='center', va='top', fontsize=12, fontweight='bold')

plt.yticks([])
plt.xticks([])
plt.title("Simplified Phylogenetic Tree\nBased on Protein Sequence Similarity", fontsize=16)
plt.xlabel("Species")
plt.ylabel("Evolutionary Distance")
plt.grid(True, alpha=0.3, linestyle='--')

tree_file = "simplified_phylogenetic_tree.png"
plt.savefig(tree_file, dpi=300, bbox_inches='tight')
print(f"✓ 进化树已保存: {tree_file}")

print("\n" + "="*60)
print("项目完成！生成的文件：")
print(f"  1. {output_file} - 蛋白质相似度热图")
print(f"  2. {tree_file} - 简化进化树")
print("\n这个演示展示了完整的生物信息学分析流程：")
print("  数据准备 → 相似度计算 → 可视化 → 进化分析")
print("="*60)

plt.show()
