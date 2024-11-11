# Estimating Pi Using Monte Carlo Method

## Overview

This project demonstrates the use of the **Monte Carlo method** to estimate the value of π (pi). It simulates random point generation within a square and calculates the proportion of points that fall inside a circle inscribed within the square.

This code was developed as part of my Probabilistic Graphical Models (PGM) course project at IASBS.

## How It Works

1. **Random Point Generation**:  
   The program generates a large number of random points within a square. 

2. **Circle Check**:  
   For each point, it calculates its distance from the origin. If the distance is less than or equal to the radius of the circle, the point lies inside the circle.

3. **Pi Estimation**:  
   Since the area of a circle is proportional to π, the ratio of points inside the circle to the total points approximates π/4. Multiplying this ratio by 4 gives an estimate for π.

## Code Breakdown

- **`checkPoint(square, circle)`**  
  Generates random points within the square and counts how many fall inside the circle.

- **`pi(insideSquare, insideCircle)`**  
  Uses the ratio of points inside the circle to total points to estimate π.

- **Main Execution**  
  The program sets the bounds for the square and circle, performs the simulation, and prints the estimated value of π.

## Usage

1. Clone the repository or copy the script.
2. Run the script using Python:
   ```bash
   python estimate_pi.py
   ```
3. The program will print an estimated value for π.

## Example Output

```plaintext
The score estimated for pi = 3.14159
```

## Dependencies

- Python 3.x
- `math` and `random` modules (standard Python libraries)

## Limitations

- **Performance**: The script uses a very high number of iterations (`1e11`), which may be computationally intensive. Consider reducing the number for faster results or testing.
- **Accuracy**: The estimation accuracy improves with more points but requires more computation.

## Future Improvements

- Add a progress bar or status updates for long simulations.
- Optimize performance by parallelizing the random point generation.
- Allow users to specify the number of iterations and the radius via command-line arguments.