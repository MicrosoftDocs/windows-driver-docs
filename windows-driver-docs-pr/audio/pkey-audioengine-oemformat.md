---
title: PKEY\_AudioEngine\_OEMFormat
description: PKEY\_AudioEngine\_OEMFormat
ms.assetid: a1587f46-1c21-4419-a1a4-81fe299c6871
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# PKEY\_AudioEngine\_OEMFormat


In Windows Vista and later, the **PKEY\_AudioEngine\_OEMFormat** property key identifies the default stream format for an audio endpoint device. Both rendering and capture devices have default formats. The global audio engine uses a device's default format to connect to the device for shared-mode operation. The INF file that installs the device loads the device's default format into the registry. The user can change the default format through the Windows multimedia control panel (Mmsys.cpl). Windows XP and previous versions of Windows do not support the **PKEY\_AudioEngine\_OEMFormat** property key.

An INF file specifies the default format for an audio endpoint device in the add-registry section for that device. The following INF example shows an add-registry section that loads the default format for an endpoint device into the registry.

```inf
;;
;; Identify endpoint device as a set of speakers.
;; Set default format to 48-kHz, 16-bit stereo.
;; Add endpoint extension property page.
;;
[OEMSettingsOverride.AddReg]
HKR,"EP\\0", %PKEY_AudioEndpoint_Association%,,%KSNODETYPE_SPEAKER%
HKR,"EP\\0", %PKEY_AudioEngine_OEMFormat%, %REG_BINARY%, 41,00,00,00,28,00,00,00,
 FE,FF,02,00,80,BB,00,00,00,EE,02,00,04,00,10,00,16,00,10,00,03,00,00,00,01,00,
 00,00,00,00,10,00,80,00,00,AA,00,38,9B,71
HKR,"EP\\0", %PKEY_AudioEndpoint_ControlPanelProvider%,,%AUDIOENDPOINT_EXT_UI_CLSID
```

The preceding example is taken from the file Sysfx.inf in the Sysfx audio sample in the Windows Driver Kit. The Strings section of this INF file contains the following definitions.

```inf
PKEY_AudioEndpoint_ControlPanelProvider = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},1"
PKEY_AudioEndpoint_Association          = "{1DA5D803-D492-4EDD-8C23-E0C0FFEE7F0E},2"
PKEY_AudioEngine_OEMFormat              = "{E4870E26-3CC5-4CD2-BA46-CA0A9A70ED04},3"
```

In the preceding example, the name of the add-registry section, OEMSettingsOverride.AddReg, is defined by an [**AddReg**](https://msdn.microsoft.com/library/windows/hardware/ff546320) directive in an interface installation section in Sysfx.inf. The preceding example adds several properties of endpoint number 0 (identified by the string "EP\\\\0") to the registry entry for the device interface. (If a device interface represents a [wave filter](https://msdn.microsoft.com/library/windows/hardware/ff538862) with more than one endpoint, the additional endpoints are numbered 1, 2, and so on.) For more information about interface installation sections, see [**INF AddInterface Directive**](https://msdn.microsoft.com/library/windows/hardware/ff546310).

After the INF file has created the three property keys and loaded their associated values into the registry, applications can access the properties by obtaining the [IPropertyStore](https://msdn.microsoft.com/library/windows/hardware/ff536954) interface for the endpoint device. Header file Mmdeviceapi.h in the Windows SDK contains C/C++ definitions of the three property keys. For more information about obtaining the IPropertyStore interface, see the description of the [**IMMDevice::OpenPropertyStore**](https://msdn.microsoft.com/library/windows/desktop/dd371412) method in the Windows SDK documentation.

In the preceding INF example, the **PKEY\_AudioEndpoint\_Association** property key identifies the KS pin category GUID for the endpoint device. The **PKEY\_AudioEndpoint\_ControlPanelProvider** property key identifies the class GUID for the COM interface object that supplies the property values to the property page in Mmsys.cpl for the endpoint device. For more information about these property keys, see the Windows SDK documentation. For more information about KS pin category GUIDs, see [Pin Category Property](https://msdn.microsoft.com/library/windows/hardware/ff537742).

In the preceding INF example, the property value that is associated with the **PKEY\_AudioEngine\_OEMFormat** property key is a 48-byte REG\_BINARY value that contains a serialized representation of the [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) or [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure that describes the format. To calculate the REG\_BINARY data value to associate with the **PKEY\_AudioEngine\_OEMFormat** property key, embed the **WAVEFORMATEX** or **WAVEFORMATEXTENSIBLE** structure in a **PropVariant** structure, and serialize the **PropVariant** structure by calling the **StgSerializePropVariant** function. For more information about the **PropVariant** structure and the **StgSerializePropVariant** function, see the Windows SDK documentation.

The following code example is a console application that prints the REG\_BINARY data that appears in the preceding INF example.

```cpp
//
// Embed a WAVEFORMATEXTENSIBLE structure in a PropVariant
// container, and print the PropVariant structure as a
// serialized stream of bytes in REG_BINARY format.
//

#include <stdio.h>
#include <wtypes.h>
#include <propidl.h>
#include <propvarutil.h>
#include <mmreg.h>
#include <ks.h>
#include <ksmedia.h>

void PrintSerializedFormat(WAVEFORMATEX *pWfx)
{
    HRESULT hr;
    PROPVARIANT var;
    SERIALIZEDPROPERTYVALUE* pVal;
    ULONG cb;

    // Create a VT_BLOB from the WAVEFORMATEX structure.
    var.vt = VT_BLOB;
    var.blob.cbSize = sizeof(*pWfx) + pWfx->cbSize;
    var.blob.pBlobData = (BYTE*)pWfx;

    // Serialize the PROPVARIANT structure. The serialized byte stream
    // will eventually be written to the registry as REG_BINARY data.
    hr = StgSerializePropVariant(&amp;var, &amp;pVal, &amp;cb);
    if (SUCCEEDED(hr))
    {
        // Write the binary data to stdout. Format the output so you can
        // copy and paste it directly into the INF file as REG_BINARY data.
        for (UINT i = 0; i < cb; i++)
        {
            BYTE b = ((BYTE*)pVal)[i];
            wprintf(L"%2.2X,", b);
        }

        wprintf(L"\n");
        CoTaskMemFree(pVal);
    }
}

//
// Use a WAVEFORMATEXTENSIBLE structure to specify the format
// for a 48-kHz, 16-bit, (2-channel) stereo audio stream.
//
void main()
{
    WAVEFORMATEXTENSIBLE wfx;

    wfx.Format.wFormatTag = WAVE_FORMAT_EXTENSIBLE;
    wfx.Format.nChannels = 2;
    wfx.Format.nSamplesPerSec = 48000;
    wfx.Format.nAvgBytesPerSec = 4*48000;
    wfx.Format.nBlockAlign = 4;
    wfx.Format.wBitsPerSample = 16;
    wfx.Format.cbSize = sizeof(WAVEFORMATEXTENSIBLE) - sizeof(WAVEFORMATEX);
    wfx.Samples.wValidBitsPerSample = 16;
    wfx.dwChannelMask = 3;
    wfx.SubFormat = KSDATAFORMAT_SUBTYPE_PCM;

    PrintSerializedFormat(&amp;wfx.Format);
}
```

The main function in the preceding code example creates a [**WAVEFORMATEXTENSIBLE**](https://msdn.microsoft.com/library/windows/hardware/ff538802) structure to describe the default format. You can modify the main function to create a [**WAVEFORMATEX**](https://msdn.microsoft.com/library/windows/hardware/ff538799) or **WAVEFORMATEXTENSIBLE** structure to describe the default format for your endpoint device.

The PrintSerializedFormat function in the preceding code example serializes the format description and prints the serialized format description as REG\_BINARY data. You can copy the printed output produced by the function and paste it into your INF file.

 

 





