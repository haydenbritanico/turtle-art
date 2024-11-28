import turtle
import random as r

# Pizza definition
pizza = {"toppings": ["mushroom", "pepperoni", "sausage"],
    "size": ["small", "medium", "large"]}


# Create two distinct turtles
joao = turtle.Turtle()
freddy = turtle.Turtle()

# Function to draw an irregular pizza base (triangle) with a specific color
def pizza_bot(t, color, size):
    # Draw an irregular triangle for the pizza base
    t.begin_fill()
    t.fillcolor(color)
    
    # Triangle's side lengths
    if size == "small":
        side_length = 250
    elif size == "medium":
        side_length = 275
    else:  # large size
        side_length = 300


    for _ in range(3):
        t.left(120)
        t.forward(side_length)
    
    t.end_fill()
    
    # Add toppings randomly
    for _ in range(r.randint(5,10)):  # Random number of toppings
        topping = r.choice(pizza["toppings"])
        draw_topping(t, topping)

# Function to draw toppings at random positions
def draw_topping(t, topping):
    t.penup()
    t.left(120)
    t.forward(r.randint(150,200))# Random movement to place the topping
    t.pendown()
    
    # Draw the topping based on its name
    if topping == "mushroom":
        t.dot(20, "brown")  # Mushroom (brown dot)
    elif topping == "pepperoni":
        t.dot(20, "red")  # Pepperoni (red dot)
    elif topping == "sausage":
        t.dot(20, "gray")  # Sausage (gray dot)

# Function to draw the pizza for two distinct turtles
def draw_pizzas():
    # Joao draws a medium pizza with a cheesy crust and random toppings
    pizza_bot(joao, "yellow", r.choice(pizza["size"]))
    
    # Freddy adds random toppings to Joao's pizza
    draw_topping(freddy)

draw_pizzas()
joao.hideturtle()
freddy.hideturtle()
