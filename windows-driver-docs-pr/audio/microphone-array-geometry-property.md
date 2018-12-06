---
title: Microphone Array Geometry Property
description: Microphone Array Geometry Property
ms.assetid: 7f280677-f86d-4687-b992-e2580046bd57
keywords:
- mic array WDK audio
- geometry descriptor WDK audio
- microphone array WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Microphone Array Geometry Property


In Windows Vista and later, support is provided for microphone arrays. In most situations, a single microphone embedded in a laptop or monitor does not capture sound very well. An array of microphones performs better to isolate a sound source and reject ambient noise and reverberation. The [**KSPROPERTY\_AUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537289) property specifies the geometry of a microphone array. The property value, [**KSAUDIO\_MIC\_ARRAY\_GEOMETRY**](https://msdn.microsoft.com/library/windows/hardware/ff537087), describes the array type (linear, planar, and so on), the number of microphones in the array and other features.

This topic describes how external USB microphone arrays can use the microphone array support provided with Windows Vista. An external USB microphone array must provide the parameters required to describe the geometry and other features of its array in response to a [GET\_MEM](https://go.microsoft.com/fwlink/p/?linkid=143724) request.

The USB microphone array uses a standard format to provide the geometry information. The Windows Vista USB audio class driver must use the same format when it reads the geometry information. For more information about the standard format, see [Microphone Array Geometry Descriptor Format](microphone-array-geometry-descriptor-format.md).

An application can call [IPart::GetSubType](https://go.microsoft.com/fwlink/p/?linkid=143726) to retrieve information about a jack to determine if the device plugged into the jack is a microphone array. **IPart::GetSubType** returns a pin-category GUID that represents the input jack type. If the device that is plugged in is a microphone array, the returned GUID is equal to KSNODETYPE\_MICROPHONE\_ARRAY. The application can also help you determine whether you plugged your microphone array into the wrong jack. In the latter scenario, the returned pin-category GUID is either for a different device or it indicates that there is no device plugged into the microphone jack. For more information about the pin category GUIDs, see [Pin Category Property](pin-category-property.md).

After an application discovers a microphone array that is plugged into the correct input jack, the next step is to determine the geometry of the array. There are three basic geometries: *linear*, *planar*, and *three dimensional (3-D)*. The geometry information also provides details such as the frequency range and x-y-z coordinates of each microphone.

The following code example shows a KSAUDIO\_MIC\_ARRAY\_GEOMETRY structure that an audio driver uses to describe an external USB microphone array:

```cpp
KSAUDIO_MIC_ARRAY_GEOMETRY mic_Array =
{
 0x100,// usVersion (1.0)
 KSMICARRAY_MICARRAYTYPE_LINEAR,// usMicArrayType
 7854,  // wVerticalAngleBegin (45 deg; PI/4 radians x 10000)
 -7854,  // wVerticalAngleEnd
 0, // lHorizontalAngleBegin
 0, // lHorizontalAngleEnd
 25, // usFrequencyBandLo in Hz
 19500, // usFrequencyBandHi in Hz
 2,  // usNumberOfMicrophones
 ar_mic_Coordinates // KsMicCoord
};
```

In the preceding code example, the ar\_mic\_Coordinates variable is an array of the KSAUDIO\_MICROPHONE\_COORDINATES structure and it contains the coordinates for the microphones in the microphone array.

The following code example shows how the ar\_mic\_Coordinates array is used to describe the geometric locations of the microphones in the microphone array as described in the preceding code example:

```cpp
KsMicCoord ar_mic_Coordinates[] =
{
 // Array microphone 1
 {
  KSMICARRAY_MICTYPE_CARDIOID,// usType
  100, // wXCoord (mic elements are 200 mm apart)
  0,// wYCoord 
  0, // wZCoord 
  0,// wVerticalAngle
  0,// wHorizontalAngle
 },
 // Array microphone 2
 {
  KSMICARRAY_MICTYPE_CARDIOID,// usType
  -100, // wXCoord 
  0,// wYCoord 
  0, // wZCoord 
  0,// wVerticalAngle
  0,// wHorizontalAngle
 }
};
```

In the preceding code example, the x-y-z coordinates are given for each microphone in the microphone array, together with the vertical and horizontal angles that describe their effective work areas.

To modify the Micarray MSVAD sample driver to provide array geometry information for a virtual microphone array, you must perform the following tasks.

First, navigate to Src\\Audio\\Msvad\\Micarray and locate the Mintopo.cpp file. Edit the property handler section in Mintopo.cpp so that the KSAUDIO\_MIC\_ARRAY\_GEOMETRY structure contains information about the microphone array. The specific section of code that you must modify is shown in the following code example:

```cpp
// Modify this portion of PropertyHandlerMicArrayGeometry
PKSAUDIO_MIC_ARRAY_GEOMETRY pMAG = (PKSAUDIO_MIC_ARRAY_GEOMETRY)PropertyRequest->Value;

// fill in mic array geometry fields
pMAG->usVersion = 0x0100;           // Version of Mic array specification (0x0100)
pMAG->usMicArrayType = (USHORT)KSMICARRAY_MICARRAYTYPE_LINEAR;        // Type of Mic Array
pMAG->wVerticalAngleBegin = -7854;  // Work Volume Vertical Angle Begin (-45 degrees)
pMAG->wVerticalAngleEnd   =  7854;  // Work Volume Vertical Angle End   (+45 degrees)
pMAG->wHorizontalAngleBegin = 0;    // Work Volume Horizontal Angle Begin
pMAG->wHorizontalAngleEnd   = 0;    // Work Volume Horizontal Angle End
pMAG->usFrequencyBandLo = 100;      // Low end of Freq Range
pMAG->usFrequencyBandHi = 8000;     // High end of Freq Range
 
pMAG->usNumberOfMicrophones = 2;    // Count of microphone coordinate structures to follow.

pMAG->KsMicCoord[0].usType = (USHORT)KSMICARRAY_MICTYPE_CARDIOID;          
pMAG->KsMicCoord[0].wXCoord = -100; // mic elements are 200 mm apart
pMAG->KsMicCoord[0].wYCoord = 0;         
pMAG->KsMicCoord[0].wZCoord = 0;         
pMAG->KsMicCoord[0].wVerticalAngle = 0;  
pMAG->KsMicCoord[0].wHorizontalAngle = 0;

pMAG->KsMicCoord[1].usType = (USHORT)KSMICARRAY_MICTYPE_CARDIOID;          
pMAG->KsMicCoord[1].wXCoord = 100;  // mic elements are 200 mm apart
pMAG->KsMicCoord[1].wYCoord = 0;         
pMAG->KsMicCoord[1].wZCoord = 0;         
pMAG->KsMicCoord[1].wVerticalAngle = 0;  
pMAG->KsMicCoord[1].wHorizontalAngle = 0;
```

The preceding code example shows information that was provided for a linear microphone array that has two microphone elements, each of which is a cardioid type and located 100 mm from the center of the array.

For the second modification, edit the Msvad.inf file as shown in [Modified INF for MSVAD Micarray](modified-inf-for-msvad-micarray.md).

After you complete the file modifications, complete the following procedure to build and install the sample driver for the microphone array.

1.  Start the WDK build environment in which you want to work. For example, the x86 Free Build Environment.

2.  Navigate to the Src\\Audio\\Msvad folder.

3.  Type the **build** command, and then press Enter.

4.  Copy the modified Msvad.inf file to the following folder that was created by the build process:

    Src\\Audio\\Msvad\\Micarray\\objfre\_wlh\_x86\\i386

5.  Verify that the folder in Step 4 contains a file called Vadarray.sys.

6.  Open the Control Panel and use **Add Hardware** to manually install the sample driver.

7.  Open the **Sound** applet in Control Panel and click the **Recording** tab to verify that you can see the virtual microphone array you just installed.

For information about how to develop an application to discover microphone arrays, see Appendix C of [How to Build and Use Microphone Arrays for Windows Vista](https://go.microsoft.com/fwlink/p/?linkid=306613).

 

 




