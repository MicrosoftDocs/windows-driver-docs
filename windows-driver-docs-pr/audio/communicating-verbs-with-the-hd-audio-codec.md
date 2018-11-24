---
title: Communicating Verbs with the HD Audio Codec
description: Communicating Verbs with the HD Audio Codec
ms.assetid: d93013fa-5b09-4616-bc71-5d3838337717
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Communicating Verbs with the HD Audio Codec


The IOCTL\_AZALIABUS\_SENDVERBS IOCTL is used by the Hdau.exe pin configuration tool when you define sound topologies for your audio adapters. Do not use this IOCTL for other purposes. This information about IOCTL\_AZALIABUS\_SENDVERBS is provided to document its design and implementation only. This IOCTL is supported in the Windows 7 Hdaudio.sys audio class driver.

High definition (HD) audio codecs are able to receive and respond to verbs. These verbs and the responses of the codecs to these verbs are documented as part of [The HD Audio Specification](https://go.microsoft.com/fwlink/p/?linkid=169394).

In Windows 7 and later versions of the Windows operating systems, the HD audio class driver uses the IOCTL\_AZALIABUS\_SENDVERBS IOCTL to communicate verbs with the audio codec. IOCTL\_AZALIABUS\_SENDVERBS is defined as shown in the following example:

```cpp
#define IOCTL_AZALIABUS_SENDVERBS CTL_CODE(FILE_DEVICE_UNKNOWN, 1, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

For more information about FILE\_DEVICE\_UNKNOWN, METHOD\_BUFFERED, and FILE\_ANY\_ACCESS, see the Devioctl.h header file in the Windows SDK.

To initiate communication with the audio codec, the class driver calls the [DeviceIoControl](https://go.microsoft.com/fwlink/p/?linkid=124239) function with the following parameters.

```cpp
BOOL DeviceIoControl(
  (HANDLE) hDevice,                      // handle to device
  IOCTL_AZALIABUS_SENDVERBS,             // dwIoControlCode
  NULL,                                  // lpInBuffer
  0,                                     // nInBufferSize
  (LPVOID) lpOutBuffer,                  // output buffer
  (DWORD) nOutBufferSize,                // size of output buffer
  (LPDWORD) lpBytesReturned,             // number of bytes returned
  (LPOVERLAPPED) lpOverlapped            // OVERLAPPED structure
);
```

If the call to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) is successful, it returns a nonzero value. If the call fails or is pending (not processed immediately), **DeviceIoControl** returns a zero value. The class driver can call [GetLastError](https://go.microsoft.com/fwlink/p/?linkid=169416) for a more detailed error message.

When the audio driver must change pin configuration defaults, it can use IOCTL\_AZALIABUS\_SENDVERBS to send and receive Set and Get verbs from the audio codec. If communication with the audio codec is not about pin configuration, the audio codec only responds to the Get verb.

The following example shows a function that takes an AzCorbeEntry structure and a HANDLE as parameters and returns the AzRirbResponse from the codec.

```cpp
AzRirbEntry SendVerb(HANDLE handle, AzCorbEntry verb)
{
  UserModeCodecCommandPacket c;
  UserModeCodecResponsePacket r;
  c.NumCommands = 1;
  c.Command[0] = verb;
  DWORD BytesReturned;

//A nonzero value is returned for a successful call and it is interpreted as TRUE  
BOOL rc = DeviceIoControl(handle, IOCTL_AZALIABUS_SENDVERBS, &c, sizeof(c), &r, sizeof(r), &BytesReturned, 0);

  if(!rc)
  {
    printf("Failed to communicate with the device!\n");
    return 0;
  }

  if(BytesReturned != sizeof(r))
  {
    printf("Wrong number of bytes returned!\n");
    return 0;
  }

  return r.Response[0];
}
```

The data types and structures that are used in the previous code example are defined in the following example:

### <span id="azcorbentry"></span><span id="AZCORBENTRY"></span> AzCorbEntry

```cpp
struct AzCorbEntry
{
  ULONG Verb        : 20; // 0:19
  ULONG NodeId      : 7;  // 20:26
  ULONG IndirectNID : 1;  // 27
  ULONG LinkId      : 4;  // 28:31
  enum {Invalid = 0xffffffff};
  AzCorbEntry(ULONG x = 0)
  :
    Verb(x),
    NodeId(x >> 20),
    IndirectNID(x >> 27),
    LinkId(x >> 28) {}
  operator ULONG()
  {
    return Verb | NodeId << 20 | IndirectNID << 27 | LinkId << 28;
  }
};
```

### <span id="azrirbentry"></span><span id="AZRIRBENTRY"></span> AzRirbEntry

```cpp
struct AzRirbEntry
{
  union
  {
    struct 
    {
      ULONG Response  : 21; // 0 : 20
      ULONG SubTag    : 5; // 21 : 25
      ULONG Tag       : 6; // 26 : 31
    } UnsolicitedForm;

    ULONG Response    : 32; // 0:31
  };
  ULONG Sdi         : 4;  // 32:35
  ULONG Unsolicited : 1;  // 36
  ULONG Reserved0   : 26; // 37:62
  ULONG Valid       : 1;  // 63 note this bit only exists
                          // on the "link". The fact that the response
                          // got into memory assures that it is valid
  AzRirbEntry (ULONGLONG x = 0)
  {
    Response = x & 0xffffffff;
    Sdi = x >> 32;
    Unsolicited = x >> 36;
    Reserved0 = x >> 37;
    Valid = x >> 63;
  }
  operator ULONGLONG()
  {
    return (ULONGLONG)Response | (ULONGLONG)Sdi << 32 | (ULONGLONG)Unsolicited << 36 | (ULONGLONG)Reserved0 << 37 | (ULONGLONG)Valid << 63;
  }
};
```

The following two structures are used together with the verb transfer IOCTL to enable the command and response transfers between the audio driver and the HD audio codec.

### <span id="usermodecodeccommandpacket"></span><span id="USERMODECODECCOMMANDPACKET"></span> UserModeCodecCommandPacket

```cpp
typedef struct _UserModeCodecCommandPacket
{
  ULONG NumCommands;      // number of commands in this packet
  AzCorbEntry Command[1]; // variable length array of verbs
} UserModeCodecCommandPacket;
```

### <span id="usermodecodecresponsepacket"></span><span id="USERMODECODECRESPONSEPACKET"></span> UserModeCodecResponsePacket

```cpp
typedef struct _UserModeCodecResponsePacket
{
  ULONG NumResponses;       // on successful IOCTL, this will be updated with the number of responses.
  AzRirbEntry Response[1];  // Variable length array of responses. lpOutBuffer param to DeviceIoControl
                            // must point to sufficient space to hold this IOCTL with all its responses 
} UserModeCodecResponsePacket;
```

 

 




