---
title: Testing With SensorExplorer
description: How to use SensorExplorer for sensor testing and logging
ms.date: 01/11/2024
---

# SensorExplorer overview

SensorExplorer is an app available on the [Microsoft Store](https://www.microsoft.com/p/sensorexplorer/9pgl3xpq1tpx?activetab=pivot:overviewtab) and the app package can be accessed through [GitHub](https://github.com/microsoft/busiotools/tree/master/sensors/Tools/SensorExplorer). SensorExplorer offers tests to quickly verify the installation of supported sensors such as orientation sensors (accelerometer, simple orientation sensors, etc.) and provide detailed tables and plots that enable monitoring different sensors. SensorExplorer also provides logging that can be reviewed for debugging.

There are five modes available via the menu bar on the left-hand side in SensorExplorer:

:::image type="content" source="images/sensor-explorer-overview.png" alt-text="Screenshot of the SensorExplorer app.":::

- **Test:** Used for manual testing of supported sensors. The orientation test verifies orientation sensors are installed in the correct position and the sensor data is as expected. Other tests such as frequency, offset and jitter, are also available. The sensor data is read using the [UWP Sensors API](/uwp/api/Windows.Devices.Sensors).

- **View:** Used for viewing sensor data and properties. In this mode the app displays a data visualization from a variety of sensors such as accelerometer, compass, gyrometer, inclinometer, light sensor, and orientation sensor and shows detailed sensor information in tabular format. This provides monitoring of any abnormal behaviors of the sensors, and can also be used to set the report interval of sensors.

- **MALT:** Used for connecting to and controlling a [MALT (Microsoft Ambient Light Tool)](./testing-malt-building-a-light-testing-tool.md), a simple low-cost light testing apparatus. The tool combines a microcontroller, light sensors, and a controllable light panel to calibrate light sensors and visually measure a panel's light curve.

- **Display Enhancement Override:** Used for overriding display settings. In this mode, sliders and scenario buttons are exposed to set display brightness in a variety of ways. Ensure you select the Override Requested slider to override the display given your settings.

- **Distance:** Used for manual and automatic testing of supported human presence sensors. The manual test uses predefined distances and the automatic test uses the sensor in addition to a front-facing camera with facial detection and bounding boxes to determine the accuracy of the human presence sensor.

## Utilities

Inside of the view pane, if you select a Light Sensor, a whitepoint calculation utility will be exposed. By selecting **Manually Calculate Whitepoint**, this utility allows for running X and Y chromaticities through Microsoft's Adaptive Color algorithm. The input should be an ambient light and the output will be Windows' mapped value.

:::image type="content" source="images/ManuallyCalculateWhitepoint.png" alt-text="Screenshot showing the manually calculate whitepoint pane.":::

## How to test your sensors with SensorExplorer

Tests available for each sensor can be explored by scrolling the top menu bar, highlighted in the screenshot below as a red box.

:::image type="content" source="images/sensor-explorer-tests.png" alt-text="Screenshot showing the SensorExplorer accelerometer tests screen.":::

### SensorExplorer orientation test

This test asks you to orient the device in different directions and then checks the sensor reading accordingly. A pass/fail result will be displayed at the end of the test.

#### Before beginning orientation tests

Under the test mode, if the display rotates when the device is rotated then turn off auto-rotation on the device (Search for "Rotation Lock" in Settings and turn it on). Otherwise, auto-rotation does not need to be turned off. For more information on orientation and reference frame, see [Device Reference Frame](/windows-hardware/design/whitepapers/integrating-motion-and-orientation-sensors).

#### Starting the tests

Select the **Start** button to begin the tests. For each test you have 10 seconds to orient the device so that the arrow on the screen is pointing down toward the ground.

Note:

- You may select the icon (highlighted in the screen shot below as a red box) to hide the menu bar during the test.

- The menu bar is disabled during the test and will be enabled once the test finishes.

- For the Simple Orientation Sensor the four directions tested are face up, face down, left, and right. For all other sensors, the four directions tested are up, down, left and right.

:::image type="content" source="images/sensor-explorer-orientation.png" alt-text="Screenshot of the SensorExplorer orientation tests.":::

Once the sensor data reflects that your device is indeed in the desired orientation, a green checkmark will be displayed. And you will automatically move on to the next test.

:::image type="content" source="images/sensor-explorer-orientation-success.png" alt-text="Screenshot showing a successful SensorExplorer orientation test.":::

Otherwise, after 10 sec, a red x will be displayed as this round of tests has failed.

:::image type="content" source="images/sensor-explorer-orientation-fail.png" alt-text="Screenshot showing a failed SensorExplorer orientation test.":::

#### After the tests

Select the **Save Log** button to save the log file. Data for all rounds of tests will be saved. Select the **Restart** button to start another test.

### Frequency Test

Calculates the number of sensor readings received/60 seconds. A numeric value will be displayed at the end of the test.

### Offset Test

Calculates the average error in sensor readings compared with the expected value. A numeric value will be displayed at the end of the test.

### Jitter Test

Calculates the maximum difference in sensor readings during a period of time, compared with the initial reading. A numeric value will be displayed at the end of the test.

### Resolution Noise Density Test

This test checks actual sensor resolution and noise of the physical accelerometer sensor in the device. A numeric value will be displayed at the end of the test.

## How to monitor your sensors

The **View** mode automatically detects any sensors that are attached to or embedded in the platform and displays the information read from the sensors. Scroll the top menu bar (highlighted in the screen shot below as a red box) to change the sensor being displayed. For each sensor the current data and properties are shown in a table and plotted as moving waveforms. The report interval of a specific sensor can be changed here.

:::image type="content" source="images/sensor-explorer-table.png" alt-text="Screenshot of SensorExplorer View mode.":::

## Additional information on logging

The **Save Log** button prompts for the name and location of the Event Trace Log (ETL) file, with the default name *SensorExplorerLog*. To view the ETL file use the [tracerpt command](/windows-server/administration/windows-commands/tracerpt_1).

:::image type="content" source="images/sensor-explorer-log.png" alt-text="Screenshot of the SensorExplorer log Save As dialog.":::

The following data is logged:

- Properties of the selected sensor

- Information about each test

- For orientation tests:
  - The sensor reading when a test is passed
  - The last sensor reading before the countdown ends when a test fails

- For other tests:
  - All sensor readings collected during the test
  - The final result
