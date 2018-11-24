---
title: Read data from hardware
description: This topic shows you how the sample sensor driver reads data from the sensor hardware (the accelerometer) in response to read requests.
ms.assetid: 4C01324D-3C4D-4028-A7DE-0AD8F2233071
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Read data from hardware


This topic shows you how the sample sensor driver reads data from the sensor hardware (the accelerometer) in response to read requests.

Typically the “top end” of the sensor driver is designed to be accessible to applications that can connect to the sensor, to read data. In the sample sensor driver, the “top end” of the driver is directly tied to a data reading function for reading sample data from the accelerometer. The following sections explain how data reading was implemented in the sample sensor driver.

## Handle read requests


1. Click the *client.cpp* file to open it, and find the **OnInterruptIsr** function.
2. Find the following code:

```cpp
// Read the Interrupt source
   BYTE IntSrcBuffer = 0;
   WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
   Status = I2CSensorReadRegister(pAccDevice->m_I2CIoTarget, ADXL345_INT_SOURCE, &IntSrcBuffer, sizeof(IntSrcBuffer));
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);
```

The preceding code first acquires a lock on the device, and then it determines the source of the interrupt, using the **I2CSensorReadRegister** function. The code finally releases the lock on the device.

3. Find the following code:

```cpp
// Create work item
   InterruptRecognized = TRUE;

   BOOLEAN WorkItemQueued = WdfInterruptQueueWorkItemForIsr(Interrupt);
   TraceVerbose("%!FUNC! Work item %s queued for interrupt", WorkItemQueued ? "" : " already");
```

After the sensor driver successfully determines the source of the interrupt, the sensor driver uses **WdfInterruptQueueWorkItemForIsr** to create a queued work item for the framework.

## Read sensor data


The sample sensor driver uses **GetData** to retrieve the sensor instance, acquire a lock on the device, and then read the sensor data. When the **GetData** function call returns, the lock is released.

1. Within the *client.cpp* file, find the **OnInterruptWorkItem** function. Then within that function, review the following code:

```cpp
// Invoke the function that Reads the device data
   WdfInterruptAcquireLock(Interrupt);
   Status = pAccDevice->GetData();
   WdfInterruptReleaseLock(Interrupt);
```

2. Find the **GetData** function, and find the following code:
   ```cpp
   // Read the device data
   BYTE DataBuffer[ADXL345_DATA_REPORT_SIZE_BYTES];
   WdfWaitLockAcquire(m_I2CWaitLock, NULL);
   Status = I2CSensorReadRegister(m_I2CIoTarget, ADXL345_DATA_X0, &DataBuffer[0], sizeof(DataBuffer));
   WdfWaitLockRelease(m_I2CWaitLock);
   ```

The preceding code sets aside a buffer of size *DataBuffer*, and reads the device data into that buffer, via an I2C connection.

3. Find the following code:
   ```cpp
   // Add timestamp
   FILETIME Timestamp = {};
   GetSystemTimeAsFileTime(&Timestamp);
   InitPropVariantFromFileTime(&Timestamp, &(m_pSensorData->List[SENSOR_DATA_TIMESTAMP].Value));

   SensorsCxSensorDataReady(m_SensorInstance, m_pSensorData);
   ```

The preceding code adds a time stamp to the device data, then saves the data to a location in the device context, and uses *m\_pSensorData* to point to it. This makes the data available further up the stack, to the class extension.

4. Close the *client.cpp* file.
 

 




