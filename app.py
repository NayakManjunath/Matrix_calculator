import streamlit as st
import numpy as np

st.set_page_config(page_title="Matrix Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Matrix Calculator")
st.markdown("Perform matrix operations easily using **NumPy + Streamlit**.")

st.sidebar.header("⚙️ Settings")
operation = st.sidebar.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Element-wise Multiplication", "Dot Product", "Transpose", "Determinant", "Inverse"]
)

# Function to convert user input into NumPy array
def parse_matrix_input(input_text):
    try:
        rows = [list(map(float, row.strip().split())) for row in input_text.strip().split("\n") if row.strip()]
        return np.array(rows)
    except Exception:
        st.error("Invalid matrix input. Ensure rows are separated by new lines and elements by spaces.")
        return None

st.subheader("Matrix A")
matrix_a_input = st.text_area(
    "Enter Matrix A (rows separated by newline, elements by space):",
    placeholder="e.g.\n1 2 3\n4 5 6"
)

st.subheader("Matrix B (if applicable)")
matrix_b_input = st.text_area(
    "Enter Matrix B (rows separated by newline, elements by space):",
    placeholder="e.g.\n7 8 9\n10 11 12"
)

if st.button("Calculate"):
    A = parse_matrix_input(matrix_a_input)
    B = parse_matrix_input(matrix_b_input) if matrix_b_input.strip() else None

    if A is None:
        st.stop()

    st.write("### Matrix A")
    st.dataframe(A)

    if B is not None:
        st.write("### Matrix B")
        st.dataframe(B)

    st.divider()

    try:
        if operation == "Addition":
            if B is not None:
                result = A + B
                st.success("**Result (A + B):**")
                st.dataframe(result)
            else:
                st.warning("Matrix B is required for addition.")

        elif operation == "Subtraction":
            if B is not None:
                result = A - B
                st.success("**Result (A - B):**")
                st.dataframe(result)
            else:
                st.warning("Matrix B is required for subtraction.")

        elif operation == "Element-wise Multiplication":
            if B is not None:
                result = A * B
                st.success("**Result (A * B):**")
                st.dataframe(result)
            else:
                st.warning("Matrix B is required for element-wise multiplication.")

        elif operation == "Dot Product":
            if B is not None:
                result = np.dot(A, B)
                st.success("**Result (A · B):**")
                st.dataframe(result)
            else:
                st.warning("Matrix B is required for dot product.")

        elif operation == "Transpose":
            st.success("**Transpose of A:**")
            st.dataframe(A.T)
            if B is not None:
                st.info("**Transpose of B:**")
                st.dataframe(B.T)

        elif operation == "Determinant":
            if A.shape[0] == A.shape[1]:
                det_a = np.linalg.det(A)
                st.success(f"**Determinant of A:** {det_a:.3f}")
            else:
                st.error("Matrix A must be square to compute the determinant.")

        elif operation == "Inverse":
            if A.shape[0] == A.shape[1]:
                try:
                    inv_a = np.linalg.inv(A)
                    st.success("**Inverse of A:**")
                    st.dataframe(inv_a)
                except np.linalg.LinAlgError:
                    st.error("Matrix A is not invertible (determinant = 0).")
            else:
                st.error("Matrix A must be square to compute the inverse.")

    except ValueError as e:
        st.error(f"Value Error: {e}")
    except Exception as e:
        st.error(f"Unexpected Error: {e}")



# import numpy as np

# # Function to get matrix input
# def get_matrix():
#     try:
#         rows = int(input("Enter the number of rows: "))
#         cols = int(input("Enter the number of columns: "))
#         print("Enter the matrix elements row by row:")

#         elements = []
#         for _ in range(rows):
#             row = list(map(float, input().split()))
#             if len(row) != cols:
#                 raise ValueError("Number of columns doesn't match.")
#             elements.append(row)

#         return np.array(elements)

#     except ValueError as e:
#         print(f"Error: {e}")
#         return None


# # Matrix Operations
# def matrix_operations(A, B):
#     print("\nMatrix A:\n", A)
#     print("\nMatrix B:\n", B)

#     try:
#         print("\nAddition:\n", A + B)
#     except ValueError:
#         print("Addition: Matrices must have the same dimensions.")

#     try:
#         print("\nSubtraction:\n", A - B)
#     except ValueError:
#         print("Subtraction: Matrices must have the same dimensions.")

#     try:
#         print("\nElement-wise Multiplication:\n", A * B)
#     except ValueError:
#         print("Element-wise Multiplication: Matrices must have the same dimensions.")

#     try:
#         print("\nDot Product:\n", np.dot(A, B))
#     except ValueError:
#         print("Dot Product: Number of columns in A must equal the number of rows in B.")

#     print("\nTranspose of A:\n", A.T)
#     print("\nTranspose of B:\n", B.T)

#     try:
#         print("\nDeterminant of A:\n", np.linalg.det(A))
#     except np.linalg.LinAlgError:
#         print("Determinant of A: Not applicable (Matrix must be square).")

#     try:
#         print("\nInverse of A:\n", np.linalg.inv(A))
#     except np.linalg.LinAlgError:
#         print("Inverse of A: Not invertible (Matrix must be square and non-singular).")


# # Main Program
# def main():
#     print("Matrix Calculator")
#     print("=================")
#     print("\nInput Matrix A:")
#     A = get_matrix()
#     if A is None:
#         return

#     print("\nInput Matrix B:")
#     B = get_matrix()
#     if B is None:
#         return

#     matrix_operations(A, B)


# if __name__ == "__main__":
#     main()

