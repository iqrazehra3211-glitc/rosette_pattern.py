{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "983b2fea",
   "metadata": {},
   "outputs": [],
   "source": [
    "import turtle\n",
    "\n",
    "screen = turtle.Screen()\n",
    "flower = turtle.Turtle()\n",
    "flower.speed(10)\n",
    "flower.color(\"red\")\n",
    "\n",
    "for i in range(36):\n",
    "    for j in range(4):\n",
    "        flower.forward(100)\n",
    "        flower.right(90)\n",
    "    flower.right(10)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
