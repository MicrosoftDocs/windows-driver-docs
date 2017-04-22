---
title: Read data from hardware
author: windows-driver-content
description: This topic shows you how the sample sensor driver reads data from the sensor hardware (the accelerometer) in response to read requests.
ms.assetid: 4C01324D-3C4D-4028-A7DE-0AD8F2233071
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Read data from hardware


This topic shows you how the sample sensor driver reads data from the sensor hardware (the accelerometer) in response to read requests.

Typically the “top end” of the sensor driver is designed to be accessible to applications that can connect to the sensor, to read data. In the sample sensor driver, the “top end” of the driver is directly tied to a data reading function for reading sample data from the accelerometer. The following sections explain how data reading was implemented in the sample sensor driver.

## Handle read requests


1. Click the *client.cpp* file to open it, and find the **OnInterruptIsr** function.
2. Find the following code:
```ManagedCPlusPlus
// Read the Interrupt source
   BYTE IntSrcBuffer = 0;
   WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
   Status = I2CSensorReadRegister(pAccDevice->m_I2CIoTarget, ADXL345_INT_SOURCE, &amp;IntSrcBuffer, sizeof(IntSrcBuffer));
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);
```

The preceding code first acquires a lock on the device, and then it determines the source of the interrupt, using the **I2CSensorReadRegister** function. The code finally releases the lock on the device.

3. Find the following code:
```ManagedCPlusPlus
// Create work item   
   InterruptRecognized = TRUE;

   BOOLEAN WorkItemQueued = WdfInterruptQueueWorkItemForIsr(Interrupt);
   TraceVerbose("%!FUNC! Work item %s queued for interrupt", WorkItemQueued ? "" : " already");
```

After the sensor driver successfully determines the source of the interrupt, the sensor driver uses **WdfInterruptQueueWorkItemForIsr** to create a queued work item for the framework.

## Read sensor data


The sample sensor driver uses **GetData** to retrieve the sensor instance, acquire a lock on the device, and then read the sensor data. When the **GetData** function call returns, the lock is released.

1. Within the *client.cpp* file, find the **OnInterruptWorkItem** function. Then within that function, review the following code:
```ManagedCPlusPlus
// Invoke the function that Reads the device data
   WdfInterruptAcquireLock(Interrupt);
   Status = pAccDevice->GetData();
   WdfInterruptReleaseLock(Interrupt);
```

2. Find the **GetData** function, and find the following code:
```ManagedCPlusPlus
// Read the device data
   BYTE DataBuffer[ADXL345_DATA_REPORT_SIZE_BYTES];
   WdfWaitLockAcquire(m_I2CWaitLock, NULL);
   Status = I2CSensorReadRegister(m_I2CIoTarget, ADXL345_DATA_X0, &amp;DataBuffer[0], sizeof(DataBuffer));
   WdfWaitLockRelease(m_I2CWaitLock);
```

The preceding code sets aside a buffer of size *DataBuffer*, and reads the device data into that buffer, via an I2C connection.

3. Find the following code:
```ManagedCPlusPlus
// Add timestamp
   FILETIME Timestamp = {};
   GetSystemTimeAsFileTime(&amp;Timestamp);
   InitPropVariantFromFileTime(&amp;Timestamp, &amp;(m_pSensorData->List[SENSOR_DATA_TIMESTAMP].Value));

   SensorsCxSensorDataReady(m_SensorInstance, m_pSensorData);
```

The preceding code adds a time stamp to the device data, then saves the data to a location in the device context, and uses *m\_pSensorData* to point to it. This makes the data available further up the stack, to the class extension.

4. Close the *client.cpp* file.
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Read%20data%20from%20hardware%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


