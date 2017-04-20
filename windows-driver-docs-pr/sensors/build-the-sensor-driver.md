---
title: Build the sensor driver
author: windows-driver-content
description: This topic shows you how to build the sample sensor driver for the ADXL345 accelerometer.
ms.assetid: F9D8D124-DAD6-4779-9F03-B1743BADC31A
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Build%20the%20sensor%20driver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


