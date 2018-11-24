---
title: Build the sensor driver
description: This topic shows you how to build the sample sensor driver for the ADXL345 accelerometer.
ms.assetid: F9D8D124-DAD6-4779-9F03-B1743BADC31A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Build the sensor driver


This topic shows you how to build the sample sensor driver for the ADXL345 accelerometer.

## Download the driver files


Navigate to the [Microsoft / Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples) site on GitHub, then perform the following tasks to download and build the sample sensor driver. The exercises in this topic assume that you have Microsoft Visual Studio 2015 installed on your development computer. If not, visit [this download site](https://www.visualstudio.com/downloads/visual-studio-2015-downloads-vs.aspx) for information about how to download a copy of Microsoft Visual Studio.

1. Create a folder on your development computer for the sample sensor driver files that you will download.

2. In the right-hand pane on the [Microsoft / Windows-driver-samples](https://github.com/Microsoft/Windows-driver-samples) site, click **Download ZIP**.

3. On the file save prompt across the bottom of your screen, click **Save**. The zip file will be downloaded and saved to the default location, which is the **Downloads** folder.

4. Navigate to the **Downloads** folder, then find and right-click the folder called *Windows-driver-samples-master*. Select **Extract All**. Note that this master zip file contains driver samples for many different technologies, not just for sensors.

5. In the **Extract Compressed (Zipped) Folders** window, click **Extract**. The files will be extracted into a folder that is also called **Windows-driver-samples-master**, in the **Downloads** folder. Note that this is a large file, and it can take a few minutes to extract all the files.

6. Open the **Windows-driver-samples-master** folder, then find and open the **sensors** folder.

7. In the **sensors** folder, open the **ADXL345Acc** folder, and copy all the files in this folder, and paste them into the project folder that you created in **Step 1**.

## Build the driver in Visual Studio


1. In Visual Studio, click **File** &gt; **Open** &gt; **Project/Solutions**.

2. In the **Open Project** window, navigate to your project folder, and find the contents of the sensors samples. Then open the **ADXL345Acc**, and double-click the *ADXL345Acc* solution file.

3. Click **Build** &gt; **Build Solution** to build the sample driver for the ADXL345 accelerometer.

4. When the build is complete, check the **Output** window to make sure that there are no Build errors. If there are errors, resolve them, and then click **Build** &gt; **Rebuild Solution**.

5. Using **File Explorer**, navigate to your project folder, and open the **Debug** folder that was created by the Build process.

6. In the **Debug**, open the **ADXL345Acc** folder, and check to make sure that you can see the following three files:

-   *adxl345acc.cat* - a security catalog file.

-   *ADXL345Acc.dll* - an application extension. This is the actual sensor driver.

-   *ADXL345Acc.inf* - a setup information file.

7. Copy these three files from the **ADXL345Acc** folder onto a flash drive, then follow the steps in [Install the sensor driver](install-the-sensor-driver.md) to install the sample sensor driver for the ADXL345 accelerometer.
 

 




