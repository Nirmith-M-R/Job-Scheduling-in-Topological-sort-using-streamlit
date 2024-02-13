from collections import defaultdict
import streamlit as st

class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices
		self.stack = []

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def topologicalSortUtil(self, v, visited, stack):

		visited[v] = True

		for i in self.graph[v]:
			if not visited[i]:
				self.topologicalSortUtil(i, visited, stack)

		stack.append(v)

	def topologicalSort(self):
		visited = [False]*self.V
		self.stack = []

		for i in range(self.V):
			if not visited[i]:
				self.topologicalSortUtil(i, visited, self.stack)

		print(self.stack[::-1])


if __name__ == '__main__':
	print("Following is a Topological Sort of the given graph")

	st.header("Job Scheduling using Topological Sort")
	with st.expander("Example of input :arrow_down:"):
		st.write("Number of Vertices = 6")
		st.image("image.png")
		st.write("Edge:")
		st.write("(5,2)\n(5,0)\n(4,0)\n(4,1)\n(2,3)\n(3,1)")
	vertex = st.number_input("Enter number of Vertices", min_value=3, max_value=100)
	g = Graph(vertex)

	job = [0 for v in range(vertex)]
	for i in range(vertex):
		t = st.text_input(f"Enter name of Job{i}", key=-1*(i+1))
		job[i] = t

	col1, col2 = st.columns(2)
	for i in range(vertex):
		edge = []
		with col1:
			head = st.number_input(f"Enter head {i}", key=i, min_value=0, max_value=10)
		edge.append(head)
		with col2:
			tail = st.number_input(f"Enter tail {i}", key=(i+vertex), min_value=0, max_value=10)
		edge.append(tail)
		g.addEdge(edge[0], edge[1])

	g.topologicalSort()
	lst = g.stack[::-1]
	st.subheader("Order of Job performed")
	for i in range(len(lst)):
		st.write(f"{job[lst[i]]}")
