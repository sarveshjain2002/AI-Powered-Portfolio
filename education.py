import streamlit as st

def education():
    st.title("Education🧑‍🎓: Sarvesh Udapurkar")
    
    st.write("---")
    
    # Create the table with improved HTML and CSS for better visibility
    st.markdown("""
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1em;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }
        th {
            background-color: #4CAF50;
            # color: white;
        }
        tr:nth-child(even) {
            # background-color: #f9f9f9;
        }
        tr:hover {
            # background-color: #f1f1f1;
        }
    </style>
    <table>
        <thead>
            <tr>
                <th>Sr. No.</th>
                <th>Qualification</th>
                <th>Institution</th>
                <th>Percentage/CGPA</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Bachelor of Engineering in Computer Science</td>
                <td>P. R. Pote College of Engineering and Management</td>
                <td>9.28 CGPA (82.58% Aggregate)</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Higher Secondary Certificate (HSC)</td>
                <td>Ushabai Deshmukh Junior College</td>
                <td>68.15%</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Secondary School Certificate (SSC)</td>
                <td>Gurukul Public School</td>
                <td>84.00%</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    education()





