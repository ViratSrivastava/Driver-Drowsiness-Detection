# Driver Drowsiness Detection System

This release provides tools for detecting driver drowsiness using a webcam or video input. It includes a **Windows executable** for testing and visualization and a **Debian package** for deployment on embedded systems.

## Files in this Release

1. **`driver-drowsiness-windows-beta.exe`**  
   - A Windows application to visualize and test the system's performance.
   - Allows testing with live webcam feeds or pre-recorded video files.

2. **`driver-drowsiness-detection.deb`**  
   - A Debian package for deploying the detection system on embedded platforms.

---

## Instructions for Use

### Windows
1. Download and run the `driver-drowsiness-windows-beta.exe`.
2. Select an input source (e.g., a video file or webcam feed).
3. View real-time drowsiness detection on the interface.
4. Adjust configurations as needed in the settings panel.

### Debian
1. Install the `.deb` package using the command:
   ```bash
   sudo dpkg -i driver-drowsiness-detection.deb
   ```
2. Run the program with:
   ```bash
   driver-drowsiness-detection
   ```
3. For embedded systems, connect the required hardware and configure accordingly.

---

## Feedback and Support
If you encounter any issues or have suggestions, please create an issue on this repository or contribute directly to the code.
