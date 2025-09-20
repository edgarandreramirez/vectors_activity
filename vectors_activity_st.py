import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as patches

sizeofplots=(3,3) # Size for all plots


tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = \
    st.tabs(["Instruction", "Components 2D", "Magnitude and angle", "Sum 2D", "Subtraction 2D","Sum and subtraction 2D" , "Components 3D", "Sum 3D","Subtraction 3D"])


with tab1:
    st.header("Instruction")
    
    st.header("_Vectors_ are :blue[cool] :sunglasses:")

    st.text(
    'Instructions: This Activity is to practice algebraic operations with vectors.\n'
    'The activity is centered in components of vectors, sum and substraction of vectors in 2D and 3D.\n'
    'A problem will be presented, if your answer is correct, continue to the next problem or practice another version.\n'
    'If your answer is incorrect, try with another version or jump to a new problem and then come back.\n'
#    'Answer all the problems until you reach the final problem to finish this activity. \n'
   # 'You will get a score at the end based on your performance.\n'
    #'You have to do the problems in order to get the total score. \n'
    )
    

    # Display a text input widget and store the user's input
    user_input = st.text_input("Please enter your name:")

    # Display the entered string
    if user_input:  # Only display if the user has entered something
        st.write(f"Hello, {user_input}! \n ")
        st.text("Take screenshot of the Correct! message that appears when your answer is correct. These captures will be the delivery. \n"
                "You have an infinite number of attempts to understand and solve the problems.\n"
                )
        st.write("Good luck! :brain:")
    
    

with tab2:
    st.header("Components 2D")
    
    score = 0  # Initialize the score counter

    st.subheader('Components of a vector', divider="rainbow")
    st.text(
    'Find the components of the given vector.\n'
    'Enter the values of the x- and y-component and press Submit.\n'
    )


    # Generate a random vector if not present
    if 'vector_a' not in st.session_state:
        st.session_state.vector_a = np.random.randint(-10, 10, size=2)

    a = st.session_state.vector_a

    # Plot the vector
    fig, ax = plt.subplots(figsize=sizeofplots)

    ax.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Given vector')

    ax.set_xlim(min(a[0], -5), max(a[0], 5))
    ax.set_ylim(min(a[1], -5), max(a[1], 5))
    ax.set_xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+1, 1))
    ax.set_yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+1, 1))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend(loc='best',borderpad=0.3)

    ax.grid(True)
    ax.set_title('Vector Components')
    st.pyplot(fig,width=500)

    # User input for vector components
    user_x = st.number_input('Enter the x component:', value=0, step=1)
    user_y = st.number_input('Enter the y component:', value=0, step=1)

    if st.button('Submit'):

        user_answer = np.array([user_x, user_y])

        # Plot comparison
        fig2, ax2 = plt.subplots(figsize=sizeofplots)
        ax2.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='r', label='Given Vector')
        ax2.quiver(0, 0, user_answer[0], user_answer[1], angles='xy', scale_units='xy', scale=1, color='m', label='User Answer')
        ax2.set_xlim(min(abs(a[0]), abs(user_answer[0]), -5), max(a[0], user_answer[0], 5))
        ax2.set_ylim(min(abs(a[1]), abs(user_answer[1]), -5), max(a[1], user_answer[1], 5))
        ax2.set_xticks(np.arange(ax2.get_xlim()[0], ax2.get_xlim()[1]+1, 1))
        ax2.set_yticks(np.arange(ax2.get_ylim()[0], ax2.get_ylim()[1]+1, 1))
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.legend(loc='best',borderpad=0.3)
        ax2.grid(True)
        ax2.set_title('Vector Components')
        st.pyplot(fig2,width=500)
        
        # Arrays comparison
        if np.allclose(user_answer, a, atol=0.01):
            st.success('Components 2D Correct!')
            score += 10  # Add 10 points for a correct answer
            #st.write(f'Your score is: {score}')
            #del st.session_state.vector_a  # Prepare for next question
            #Continue to next section (do nothing, Streamlit will proceed)
        else:
            st.error('Incorrect. Try again! Compare your result with the correct answer. Look at the projection of the vector on the x and y axes.')
        print(np.allclose(user_answer, a, atol=0.01))
        del st.session_state.vector_a  # Remove so a new vector is generated
        #st.experimental_rerun()        # Rerun to repeat the section with a new vector
 

    if st.button('Press to try again with a new vector'):
        del st.session_state.vector_a
        st.rerun()





with tab3:
    st.header("Magnitude and angle")

    # Components of a vector from magnitude and angle (Streamlit version)
    st.subheader('Components of a vector given magnitude and angle', divider="rainbow")
    st.text(
    'Calculate the components of a vector given its magnitud and angle.\n'
    'Enter the values and press Submit.\n'
    )

    if 'magnitude' not in st.session_state or 'angle_deg' not in st.session_state:
        st.session_state.magnitude = np.random.randint(1, 11)
        st.session_state.angle_deg = np.random.randint(0, 360)

    magnitude = st.session_state.magnitude
    angle_deg = st.session_state.angle_deg
    angle_rad = np.deg2rad(angle_deg)

    # Calculate the components
    x = magnitude * np.cos(angle_rad)
    y = magnitude * np.sin(angle_rad)
    vec = np.array([x, y])

    # Plot the vector
    fig, ax = plt.subplots(figsize=sizeofplots)
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', label='Given Vector')
    ax.set_xlim(min(x-1,-5), max(abs(x+1),5))
    ax.set_ylim(min(y-1,-5), max(abs(y+1),5))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    # Create the Arc patch
    arc = patches.Arc((0,0), width=2, height=2, angle=0, theta1=0, theta2=angle_deg, color='blue', linewidth=1)
    ax.add_patch(arc) # Add the arc to the axes


    #print mag and theta on plot
    ax.text(1+0.2, 0, f'{angle_deg}'+u"\u00b0", color='blue', fontsize=10) #ha='center', va='center', alpha=0.7
    ax.text(x+0.3, y+0.3,f'{magnitude}', color='r', fontsize=10,ha='center', va='center') #alpha=0.7
    ax.legend(loc='best',borderpad=0.3)
    ax.grid(True)
    ax.set_title('Magnitude and angle of a vector')
    st.pyplot(fig,width=500)


    st.write(f'**Vector magnitude:** {magnitude}')
    st.write(f'**Vector angle (degrees):** {angle_deg}')

    user_x2 = st.number_input('Enter the x component (rounded to 2 decimals):', key='user_x2', format="%.2f")
    user_y2 = st.number_input('Enter the y component (rounded to 2 decimals):', key='user_y2', format="%.2f")

    if st.button('Submit', key='submit_mag_angle'):
        user_answer2 = np.array([user_x2, user_y2])
        
        # Plot the correct vector and the user's answer
        fig3, ax3 = plt.subplots(figsize=sizeofplots)
        ax3.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='r', label='Correct Vector')
        ax3.quiver(0, 0, user_answer2[0], user_answer2[1], angles='xy', scale_units='xy', scale=1, color='m', label='User Answer')
        ax3.set_xlim(min(x,user_answer2[0],-5),max(abs(x),abs(user_answer2[0]),5))
        ax3.set_ylim(min(y,user_answer2[1],-5),max(abs(y),abs(user_answer2[1]),5))
        ax3.set_xlabel('X')
        ax3.set_ylabel('Y')
        ax3.legend(loc='best',borderpad=0.3)
        ax3.grid(True)
        ax3.set_title('Magnitude and angle of a vector')
        st.pyplot(fig3,width=500)

        # Round both arrays to 2 decimals for comparison
        if np.allclose(np.round(user_answer2, 2), np.round(vec, 2), atol=0.01):
            st.success('Magnitude and angle Correct!')
            score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')

            # Reset for new question
            #del st.session_state.magnitude
            #del st.session_state.angle_deg
        else:
            st.error('Incorrect. Try again! Use the corresponding trigonometric functions of the x and y components.')
            del st.session_state.magnitude
            del st.session_state.angle_deg

    if st.button('Try again with a new vector', key='try_again_mag_angle'):
        del st.session_state.magnitude
        del st.session_state.angle_deg
        st.rerun()






with tab4:
    st.header("Sum 2D")

    # Vector addition 2D (Streamlit version)
    st.subheader('Sum of two vectors in 2D', divider="rainbow")

    st.text(
        'Calculate the sum (a + b) of the given vectors.\n'
        'Enter the result and press Submit.'
        )


    if 'vec_a' not in st.session_state or 'vec_b' not in st.session_state:
        st.session_state.vec_a = np.random.randint(-5, 5, size=2)
        st.session_state.vec_b = np.random.randint(-5, 5, size=2)

    a = st.session_state.vec_a
    b = st.session_state.vec_b
    sum_vec = a + b

    # Plot the vectors a and b in 2D
    fig, ax = plt.subplots(figsize=sizeofplots)
    origin = [0, 0]

    ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
    ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
    #ax.quiver(*origin, sum_vec[0], sum_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a + b')


    ax.set_xlim([min(a[0], b[0], sum_vec[0], -5), max(a[0], b[0], sum_vec[0], 5)])
    ax.set_ylim([min(a[1], b[1], sum_vec[1], -5), max(a[1], b[1], sum_vec[1], 5)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sum of two vectors in 2D')
    ax.legend(loc='best',borderpad=0.3)
    ax.grid(True)
    st.pyplot(fig,width=500)

    st.text('NOTE: Vectors are frequently written in parentheses as pairs, such as [5 0] for a 2D vector or [1 2 3] for a 3D vector, which represent the vector\'s components along the x, y, and z axes.')
    #st.text(' While parentheses are common for this purpose, other notations like square brackets [x, y] or angle brackets ⟨x, y⟩ are also used, with the choice sometimes depending on the specific field or context of mathematics')

    st.write(f'**Vector a=** {a} ')
    st.write(f'**Vector b=** {b} ')


    user_sum_x = st.number_input('Enter the x component of (a + b):', key='sum_x', step=1)
    user_sum_y = st.number_input('Enter the y component of (a + b):', key='sum_y', step=1)

    if st.button('Submit', key='submit_vec_sum'):
        user_answer = np.array([user_sum_x, user_sum_y])
        
        # Plot the vectors and user answer
        fig, ax = plt.subplots(figsize=sizeofplots)
        origin = [0, 0]
        
        ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
        ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
        ax.quiver(*origin, sum_vec[0], sum_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a + b')
        ax.quiver(*origin, user_answer[0],user_answer[1], angles='xy', scale_units='xy', scale=1,color='m', label='Your Answer')
        
        ax.set_xlim([min(a[0], b[0], sum_vec[0], user_answer[0], -5), max(a[0], b[0], sum_vec[0], user_answer[0], 5)])
        ax.set_ylim([min(a[1], b[1], sum_vec[1], user_answer[1], -5), max(a[1], b[1], sum_vec[1], user_answer[1], 5)])
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Sum of two vectors in 2D')
        ax.legend(loc='best',borderpad=0.3)
        ax.grid(True)
        st.pyplot(fig,width=500)

        if np.array_equal(user_answer, sum_vec):
            st.success('Sum 2D Correct!')

            del st.session_state.vec_a
            del st.session_state.vec_b
            score += 10  # Add 10 points for a correct answer
            #st.write(f'Your score is: {score}')

        else:
            st.error('Incorrect. Try again! Sum of vectors involves adding the x-components and y-components separately.')
            del st.session_state.vec_a
            del st.session_state.vec_b

    if st.button('Try Again with a new vector (2D)', key='try_again_sum_2d'):
        del st.session_state.vec_a
        del st.session_state.vec_b
        st.rerun()







with tab5:
    st.header("Subtraction 2D")
    # Vector subtraction 2D (Streamlit version)
    st.subheader('Subtraction of two vectors in 2D', divider="rainbow")
    st.text(
    'Calculate the subtraction (a - b) of the given vectors.\n'
    'Enter the result and press Submit.\n'
    )

    if 'vecs_a' not in st.session_state or 'vecs_b' not in st.session_state:
        st.session_state.vecs_a = np.random.randint(-5, 5, size=2)
        st.session_state.vecs_b = np.random.randint(-5, 5, size=2)

    a = st.session_state.vecs_a
    b = st.session_state.vecs_b
    sub_vec = a - b

    # Plot the vectors a and b in 2D
    fig, ax = plt.subplots(figsize=sizeofplots)
    origin = [0, 0]
    
    ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
    ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
    #ax.quiver(*origin, sub_vec[0], sub_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a - b')

    ax.set_xlim([min(a[0], b[0], sub_vec[0], -5), max(a[0], b[0], sub_vec[0], 5)])
    ax.set_ylim([min(a[1], b[1], sub_vec[1], -5), max(a[1], b[1], sub_vec[1], 5)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Subtraction of vectors in 2D')
    ax.legend(loc='best',borderpad=0.3)
    ax.grid(True)
    st.pyplot(fig,width=500)

    st.write(f'**Vector a=** {a}')
    st.write(f'**Vector b=** {b}')



    user_sub_x = st.number_input('Enter the x component of (a - b):', key='sub_x', step=1)
    user_sub_y = st.number_input('Enter the y component of (a - b):', key='sub_y', step=1)

    if st.button('Submit', key='submit_vec_sub'):
        user_answer = np.array([user_sub_x, user_sub_y])
        
        # Plot the vectors and user answer
        fig, ax = plt.subplots(figsize=sizeofplots)
        origin = [0, 0]

        ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
        ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
        ax.quiver(*origin, sub_vec[0], sub_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a - b')
        ax.quiver(*origin, user_answer[0], user_answer[1], angles='xy', scale_units='xy', scale=1, color='m', label='Your Answer')

        ax.set_xlim([min(a[0], b[0], sub_vec[0], user_answer[0], -5), max(a[0], b[0], sub_vec[0], user_answer[0], 5)])
        ax.set_ylim([min(a[1], b[1], sub_vec[1], user_answer[1], -5), max(a[1], b[1], sub_vec[1], user_answer[1], 5)])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Subtraction of two vectors in 2D')
        ax.legend(loc='best',borderpad=0.3)
        ax.grid(True)
        st.pyplot(fig,width=500)

        if np.array_equal(user_answer, sub_vec):
            st.success('Subtraction 2D Correct!')

            del st.session_state.vecs_a
            del st.session_state.vecs_b
            score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')

        else:
            st.error('Incorrect. Try again! Subtraction of vectors involves subtracting the x-components and y-components separately.')
            del st.session_state.vecs_a
            del st.session_state.vecs_b

    if st.button('Try Again with a new vector (2D)', key='try_again_sub_2d'):
        del st.session_state.vecs_a
        del st.session_state.vecs_b
        st.rerun()






with tab6:
    st.header("Sum and subtraction 2D")
    # Three Vector addition 2D (Streamlit version)
    st.subheader('Sum and subtraction of three vectors in 2D', divider="rainbow")
    st.text(
        'Calculate the result of the operation (a - b + c) of the given vectors.\n'
        'Enter the result and press Submit.\n'
        )

    if 'vec3_a' not in st.session_state or 'vec3_b' not in st.session_state or 'vec3_c' not in st.session_state:
        st.session_state.vec3_a = np.random.randint(-5, 5, size=2)
        st.session_state.vec3_b = np.random.randint(-5, 5, size=2)
        st.session_state.vec3_c = np.random.randint(-5, 5, size=2)

    a = st.session_state.vec3_a
    b = st.session_state.vec3_b
    c = st.session_state.vec3_c
    sum_vec = a - b + c

    # Plot the vectors a, b, and c in 2D
    fig, ax = plt.subplots(figsize=sizeofplots)
    origin = [0, 0]

    ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
    ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
    ax.quiver(*origin, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='orange', label='c')
    #ax.quiver(*origin, sum_vec[0], sum_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a - b + c')

    ax.set_xlim([min(a[0], b[0], c[0], sum_vec[0], -5), max(a[0], b[0], c[0], sum_vec[0], 5)])
    ax.set_ylim([min(a[1], b[1], c[1], sum_vec[1], -5), max(a[1], b[1], c[1], sum_vec[1], 5)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Sum and subtraction of three vectors in 2D')
    ax.legend(loc='best',borderpad=0.3)
    ax.grid(True)
    st.pyplot(fig,width=500)

    st.write(f'**Vector a=** {a}')
    st.write(f'**Vector b=** {b}')
    st.write(f'**Vector c=** {c}')
    
    user_sum_x = st.number_input('Enter the x component of (a - b + c):', key='sum3_x', step=1)
    user_sum_y = st.number_input('Enter the y component of (a - b + c):', key='sum3_y', step=1)

    if st.button('Submit', key='submit_vec_sum3'):
        user_answer = np.array([user_sum_x, user_sum_y])
        
        # Plot the vectors and user answer
        fig, ax = plt.subplots(figsize=sizeofplots)
        origin = [0, 0]

        ax.quiver(*origin, a[0], a[1], angles='xy', scale_units='xy', scale=1, color='g', label='a')
        ax.quiver(*origin, b[0], b[1], angles='xy', scale_units='xy', scale=1, color='b', label='b')
        ax.quiver(*origin, c[0], c[1], angles='xy', scale_units='xy', scale=1, color='orange', label='c')
        ax.quiver(*origin, sum_vec[0], sum_vec[1], angles='xy', scale_units='xy', scale=1, color='r', label='a - b + c')
        ax.quiver(*origin, user_answer[0], user_answer[1], angles='xy', scale_units='xy', scale=1, color='m', label='Your Answer')

        ax.set_xlim([min(a[0], b[0], c[0], sum_vec[0], user_answer[0], -5), max(a[0], b[0], c[0], sum_vec[0], user_answer[0], 5)])
        ax.set_ylim([min(a[1], b[1], c[1], sum_vec[1], user_answer[1], -5), max(a[1], b[1], c[1], sum_vec[1], user_answer[1], 5)])
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Sum and subtraction of three vectors in 2D')
        ax.legend(loc='best',borderpad=0.3)
        ax.grid(True)
        st.pyplot(fig,width=500)

        if np.array_equal(user_answer, sum_vec):
            st.success('Sum and subtraction 2D Correct!')
            del st.session_state.vec3_a
            del st.session_state.vec3_b
            del st.session_state.vec3_c
            score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')

        else:
            st.error('Incorrect. Try again! In this case we have a combination of addition and subtraction of vectors.')
            del st.session_state.vec3_a
            del st.session_state.vec3_b
            del st.session_state.vec3_c

    if st.button('Try Again with new vectors (2D)', key='try_again_sum3_2d'):
        del st.session_state.vec3_a
        del st.session_state.vec3_b
        del st.session_state.vec3_c
        st.rerun()

if False:  # Disable this section for now 
    with tab7:
        st.header("Components 3D")
        # Components of a 3D vector
        st.subheader('Components of a vector in 3D', divider="rainbow")
        st.text(
         'Find the components of the given vector in 3D.\n'
         'Enter the result and press Submit.\n'
         )

        if 'vector_a3d' not in st.session_state:
            st.session_state.vector_a3d = np.random.randint(0, 10, size=3)

        a = st.session_state.vector_a3d

        # Plot the vector
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]

        ax.quiver(*origin, *a, color='g', label='a')
    
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_zlim(0, 10)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Components of a Vector in 3D')
        ax.legend(loc='best')

    #ax.vlines(a[0], 0, a[1], linestyle='--', color='gray')

        ax.set_box_aspect(aspect=None, zoom=0.8)
        ax.grid(True)
        st.pyplot(fig,width=500)


        # User input for vector components
        user_x = st.number_input('Enter the x component:', key='a3d_x', step=1)
        user_y = st.number_input('Enter the y component:', key='a3d_y', step=1)
        user_z = st.number_input('Enter the z component:', key='a3d_z', step=1)


        if st.button('Submit', key='submit_vec_a3d'):
            user_answer = np.array([user_x, user_y, user_z])

        # Plot comparison
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            origin = [0, 0, 0]

            ax.quiver(*origin, *a, color='g', label='a')
            ax.quiver(*origin, *user_answer, color='m', label='Your Answer')


            ax.set_xlim([0, max( user_answer[0], 10)])
            ax.set_ylim([0, max( user_answer[1], 10)])
            ax.set_zlim([0, max( user_answer[2], 10)])
    
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_ylabel('Z')
        
            ax.set_title('Components of a Vector in 3D')
            ax.legend(loc='best')

            ax.set_box_aspect(aspect=None, zoom=0.8)
            ax.grid(True)
            st.pyplot(fig,width=500)


            # Arrays comparison
            if np.array_equal(user_answer, a):
                st.success('Components 3D Correct!')
                score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')
            #        del st.session_state.vector_a  # Prepare for next question
            else:
                st.error('Incorrect. Try again! Compare your result with the correct answer. Look at the projection of the vector on the x, y and z axes.')
                del st.session_state.vector_a  # Remove so a new vector is generated
                del st.session_state.user_answer
                #st.experimental_rerun()        # Rerun to repeat the section with a new vector
 

        if st.button('Try again with a new 3D vector'):
            del st.session_state.vector_a
            st.rerun()


with tab7:
    st.header("Components 3D")
    # Components of a 3D vector given magnitude and angles
    st.subheader('Components of a vector in 3D', divider="rainbow")
    st.text(
        'Find the components of the given vector in 3D.\n'
        'Enter the result and press Submit.\n'
        )

    if 'vector_a3d' not in st.session_state:
        st.session_state.vector_a3d = np.random.randint(0, 10, size=3)

    a = st.session_state.vector_a3d
    a_magnitude = np.linalg.norm(a)
    a_theta = np.arccos(a[2]/a_magnitude)  # angle with z-axis
    a_phi = np.arctan2(a[1], a[0])  # angle in xy-plane from x-axis

    #st.write(f'Given vector (a): {a}')

    st.write(f'**Vector magnitude:** {a_magnitude:.2f}')
    st.write(f'**Angle with z-axis ($\\theta$ in degrees):** {np.degrees(a_theta):.2f}')
    st.write(f'**Angle in xy-plane from x-axis ($\\phi$ in degrees):** {np.degrees(a_phi):.2f}')


    # Plot the vector
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    origin = [0, 0, 0]

    ax.quiver(*origin, *a, color='r', label='given vector', arrow_length_ratio=0.1)
    
    ax.plot(xs=[0, a[0]], ys=[0, a[1]], zs=[0, 0],linestyle='--', color='gray')  # projection on xy-plane
    ax.plot(xs=[a[0], a[0]], ys=[a[1], a[1]], zs=[0, a[2]],linestyle='--', color='gray')  # vertical line to vector    
    ax.plot(xs=[a[0], a[0]], ys=[0, a[1]], zs=[0, 0],linestyle='--', color='gray')  # projection on x-axis
    #ax.view_init(elev=20., azim=65)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Components of a Vector in 3D')
    ax.legend(loc='best',borderpad=0.3)

    #print mag and theta on plot
    ax.text(0, 0, 2, r'$\theta$', color='blue', fontsize=10) #ha='center', va='center', alpha=0.7
    ax.text(2, 0, 0, r'$\phi$', color='blue', fontsize=10) #ha='center', va='center', alpha=0.7
    ax.text(a[0]+0.5, a[1]+0.5, a[2]+0.5, f'{a_magnitude:.2f}', color='r', fontsize=10) #ha='center', va='center', alpha=0.7
    # Create the Arc patch for theta
    #arc_theta = patches.Arc((0,0), width=2, height=2, angle=0, theta1=0, theta2=np.degrees(a_theta), color='blue', linewidth=1)
    #ax.add_patch(arc_theta) # Add the arc to the axes
    # Create the Arc patch for phi
    #arc_phi = patches.Arc((0,0), width=2, height=2, angle=0, theta1=0, theta2=np.degrees(a_phi), color='green', linewidth=1)
    #ax.add_patch(arc_phi) # Add the arc to the axes    
    

    #ax.vlines(a[0], 0, a[1], linestyle='--', color='gray')

    ax.set_box_aspect(aspect=None, zoom=0.8)
    ax.grid(True)
    st.pyplot(fig,width=500)


    # User input for vector components
    user_x = st.number_input('Enter the x component:', key='a3d_x', step=1)
    user_y = st.number_input('Enter the y component:', key='a3d_y', step=1)
    user_z = st.number_input('Enter the z component:', key='a3d_z', step=1)


    if st.button('Submit', key='submit_vec_a3d'):
        user_answer = np.array([user_x, user_y, user_z])

        # Plot comparison
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]

        ax.quiver(*origin, *a, color='r', label='given vector', arrow_length_ratio=0.1)
        ax.quiver(*origin, *user_answer, color='m', label='Your Answer',arrow_length_ratio=0.1)

        #projection of given vector
        ax.plot(xs=[0, a[0]], ys=[0, a[1]], zs=[0, 0],linestyle='--', color='gray')  # projection on xy-plane
        ax.plot(xs=[a[0], a[0]], ys=[a[1], a[1]], zs=[0, a[2]],linestyle='--', color='gray')  # vertical line to vector    
        ax.plot(xs=[a[0], a[0]], ys=[0, a[1]], zs=[0, 0],linestyle='--', color='gray')  # projection on x-axis


        ax.set_xlim([0, max( user_answer[0], 10)])
        ax.set_ylim([0, max( user_answer[1], 10)])
        ax.set_zlim([0, max( user_answer[2], 10)])
    
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_ylabel('Z')
        
        ax.set_title('Components of a Vector in 3D')
        ax.legend(loc='best',borderpad=0.3)
      
        #print mag and theta on plot
        ax.text(0, 0, 2, r'$\theta$', color='blue', fontsize=10) #ha='center', va='center', alpha=0.7
        ax.text(2, 0, 0, r'$\phi$', color='blue', fontsize=10) #ha='center', va='center', alpha=0.7
        ax.text(a[0]+0.5, a[1]+0.5, a[2]+0.5, f'{a_magnitude:.2f}', color='r', fontsize=10) #ha='center', va='center', alpha=0.7

        ax.set_box_aspect(aspect=None, zoom=0.8)
        ax.grid(True)
        st.pyplot(fig,width=500)


        # Arrays comparison
        if np.allclose(user_answer, a, atol=0.1):
            st.success('Components 3D Correct!')
            score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')
            #        del st.session_state.vector_a  # Prepare for next question
        else:
                st.error('Incorrect. Try again! Compare your result with the correct vector. Look at the projection of the vector on the xy-plane and use the appropriate trigonometric functions.')
                del st.session_state.vector_a3d  # Remove so a new vector is generated
                #del st.session_state.user_answer
                #st.experimental_rerun()        # Rerun to repeat the section with a new vector
 

    if st.button('Try again with a new 3D vector'):
        del st.session_state.vector_a3d
#        del st.session_state.user_answer
        st.rerun()




with tab8:
    st.header("Sum 3D")
    # Vector addition 3D (Streamlit version)
    st.subheader('7. Sum of two vectors in 3D', divider="rainbow")
    st.text(
    'Find the sum (a + b) of the given vectors in 3D.\n'
    'Enter the result and press Submit.\n'
    )

    if 'sum_vec_a' not in st.session_state or 'sum_vec_b' not in st.session_state:
        st.session_state.sum_vec_a = np.random.randint(0, 5, size=3)
        st.session_state.sum_vec_b = np.random.randint(0, 5, size=3)

    a = st.session_state.sum_vec_a
    b = st.session_state.sum_vec_b
    sum_vec = a + b

    # Plot the vectors a and b in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    origin = [0, 0, 0]

    
    ax.quiver(*origin, *a, color='g', label='a',arrow_length_ratio=0.1)
    ax.quiver(*origin, *b, color='b', label='b',arrow_length_ratio=0.1)
    #ax.quiver(*origin, *sum_vec, color='r', label='a + b')

    ax.set_xlim([0, max(a[0], b[0], sum_vec[0], 5)])
    ax.set_ylim([0, max(a[1], b[1], sum_vec[1], 5)])
    ax.set_zlim([0, max(a[2], b[2], sum_vec[2], 5)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Sum of Vectors in 3D')
    ax.legend(loc='best',borderpad=0.3)
    ax.set_box_aspect(aspect=None, zoom=0.8)
    ax.grid(True)
    st.pyplot(fig,width=500)

    st.write(f'**Vector a=** {a}')
    st.write(f'**Vector b=** {b}')
    
    user_sum_x = st.number_input('Enter the x component of (a + b):', key='sum3d_x', step=1)
    user_sum_y = st.number_input('Enter the y component of (a + b):', key='sum3d_y', step=1)
    user_sum_z = st.number_input('Enter the z component of (a + b):', key='sum3d_z', step=1)
    
    if st.button('Submit', key='submit_vec_sum3d'):
        user_answer = np.array([user_sum_x, user_sum_y, user_sum_z])
        
        # Plot the vectors and user answer
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        origin = [0, 0, 0]

        ax.quiver(*origin, *a, color='g', label='a',arrow_length_ratio=0.1)
        ax.quiver(*origin, *b, color='b', label='b',arrow_length_ratio=0.1)
        ax.quiver(*origin, *sum_vec, color='r', label='a + b',arrow_length_ratio=0.1)
        ax.quiver(*origin, *user_answer, color='m', label='Your Answer',arrow_length_ratio=0.1)

        ax.set_xlim([min(0, user_answer[0]), max(a[0], b[0], sum_vec[0], user_answer[0], 5)])
        ax.set_ylim([min(0, user_answer[1]), max(a[1], b[1], sum_vec[1], user_answer[1], 5)])
        ax.set_zlim([min(0, user_answer[2]), max(a[2], b[2], sum_vec[2], user_answer[2], 5)])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    
        ax.set_title('Sum of Vectors 3D')
        ax.legend(loc='best',borderpad=0.3)
    
        ax.set_box_aspect(aspect=None, zoom=0.8)
        ax.grid(True)
        st.pyplot(fig,width=500)

        if np.array_equal(user_answer, sum_vec):
            st.success('Sum 3D Correct!')
            del st.session_state.sum_vec_a
            del st.session_state.sum_vec_b
            score += 10  # Add 10 points for a correct answer
            #st.write(f'Your score is: {score}')
        else:
            st.error('Incorrect. Try again! Sum of vectors in 3D involves adding the x-components, y-components and the z-components separately.')
            del st.session_state.sum_vec_a
            del st.session_state.sum_vec_b

    if st.button('Try Again with new vectors (3D)', key='try_again_sum_3d'):
        del st.session_state.sum_vec_a
        del st.session_state.sum_vec_b
        st.rerun()




with tab9:
    st.header("Subtraction 3D")
    # Subtraction of two vectors (Streamlit version)
    st.subheader('Subtraction of two vectors in 3D', divider="rainbow")
    st.text(
    'Calculate the subtraction (a - b) of the given vectors in 3D.\n'
    'Enter the result and press Submit.\n'
    )

    if 'sub_vec_a' not in st.session_state or 'sub_vec_b' not in st.session_state:
        st.session_state.sub_vec_a = np.random.randint(0, 5, size=3)
        st.session_state.sub_vec_b = np.random.randint(0, 5, size=3)

    a = st.session_state.sub_vec_a
    b = st.session_state.sub_vec_b
    subtraction_vec = a - b

    # Plot the vectors a and b in 3D
    #import plotly.express as px
    #import matplotlib.pyplot as mpld3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    origin = [0, 0, 0]

    ax.quiver(*origin, *a, color='g', label='a',arrow_length_ratio=0.1)
    ax.quiver(*origin, *b, color='b', label='b',arrow_length_ratio=0.1)
    #ax.quiver(*origin, *subtraction_vec, color='r', label='a - b')

    ax.set_xlim([0, max(a[0], b[0], 5)])
    ax.set_ylim([0, max(a[1], b[1], 5)])
    ax.set_zlim([0, max(a[2], b[2], 5)])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Subtraction of Vectors in 3D')
    ax.legend(loc='best',borderpad=0.3)
    ax.set_box_aspect(aspect=None, zoom=0.8)
    ax.grid(True)
    #ax.view_init(elev=20., azim=30)  # Set a good view angle
    st.pyplot(fig,width=500)

    st.write(f'**Vector a=** {a}')
    st.write(f'**Vector b=** {b}')

    user_sub_x = st.number_input('Enter the x component of (a - b):', key='sub3d_x', step=1)
    user_sub_y = st.number_input('Enter the y component of (a - b):', key='sub3d_y', step=1)
    user_sub_z = st.number_input('Enter the z component of (a - b):', key='sub3d_z', step=1)

    if st.button('Submit', key='submit_vec_sub3d'):
        user_answer = np.array([user_sub_x, user_sub_y, user_sub_z])
        
        # Plot the vectors and user answer
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origin = [0, 0, 0]

        ax.quiver(*origin, *a, color='g', label='a',arrow_length_ratio=0.1)
        ax.quiver(*origin, *b, color='b', label='b',arrow_length_ratio=0.1)
        ax.quiver(*origin, *subtraction_vec, color='r', label='a - b',arrow_length_ratio=0.1)
        ax.quiver(*origin, *user_answer, color='m', label='Your Answer',arrow_length_ratio=0.1)

        ax.set_xlim([min(0, subtraction_vec[0],user_answer[0]), max(a[0], b[0], subtraction_vec[0], user_answer[0], 5)])
        ax.set_ylim([min(0, subtraction_vec[1],user_answer[1]), max(a[1], b[1], subtraction_vec[1], user_answer[1], 5)])
        ax.set_zlim([min(0, subtraction_vec[2],user_answer[2]), max(a[2], b[2], subtraction_vec[2], user_answer[2], 5)])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Subtraction of Vectors')

        ax.legend(loc='best',borderpad=0.3)
        ax.set_box_aspect(aspect=None, zoom=0.8)
        ax.grid(True)
        st.pyplot(fig,width=500)

        if np.array_equal(user_answer, subtraction_vec):
            st.success('Subtraction 3D Correct!')
            del st.session_state.sub_vec_a
            del st.session_state.sub_vec_b
            score += 10  # Add 10 points for a correct answer
            #        st.write(f'Your score is: {score}')

        else:
            st.error('Incorrect. Try again! Subtraction of vectors in 3D involves subtracting the x-components, y-components and z-components separately.')
            del st.session_state.sum_vec_a
            del st.session_state.sum_vec_b

    if st.button('Try Again with new vectors (3D)', key='try_again_sub_3d'):
        del st.session_state.sub_vec_a
        del st.session_state.sub_vec_b
        st.rerun()


# Final Score
#st.subheader('Activity Completed!', divider="rainbow")
#st.write(f'Your final score is: **{score} / 70**')
#st.write('Thank you for participating in this vector operations activity! 🎉')