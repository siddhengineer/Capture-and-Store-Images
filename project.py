import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)

# Capture an image from the camera
result, image = camera.read()

# Release the camera
camera.release()

# Check if the image was captured successfully
if not result:
    print("Failed to capture image from the camera.")
    exit()

# Save the original image to a file
original_filename = "original.jpg"
cv2.imwrite(original_filename, image)
print(f"Original image saved as {original_filename}")


# Rotate the image in all directions
rotated_images = []
directions = [cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_180]
for direction in directions:
    
        # Rotate the image
        rotated = cv2.rotate(image, direction)

        # Add the rotated image to the list
        rotated_images.append(rotated)

        # Display the rotated image
        cv2.imshow("Rotated Image", rotated)
        cv2.waitKey(500)  # Wait for 0.5 seconds before rotating again

# Save the rotated images to files
for i, rotated in enumerate(rotated_images):
    filename = f"rotated_{i + 1}.jpg"
    cv2.imwrite(filename, rotated)
    print(f"Rotated image {i + 1} saved as {filename}")

# Close all windows
cv2.destroyAllWindows()
