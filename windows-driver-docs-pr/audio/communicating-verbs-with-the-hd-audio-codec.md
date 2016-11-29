---
title: Communicating Verbs with the HD Audio Codec
description: Communicating Verbs with the HD Audio Codec
ms.assetid: d93013fa-5b09-4616-bc71-5d3838337717
---

# Communicating Verbs with the HD Audio Codec


The IOCTL\_AZALIABUS\_SENDVERBS IOCTL is used by the Hdau.exe pin configuration tool when you define sound topologies for your audio adapters. Do not use this IOCTL for other purposes. This information about IOCTL\_AZALIABUS\_SENDVERBS is provided to document its design and implementation only. This IOCTL is supported in the Windows 7 Hdaudio.sys audio class driver.

High definition (HD) audio codecs are able to receive and respond to verbs. These verbs and the responses of the codecs to these verbs are documented as part of [The HD Audio Specification](http://go.microsoft.com/fwlink/p/?linkid=169394).

In Windows 7 and later versions of the Windows operating systems, the HD audio class driver uses the IOCTL\_AZALIABUS\_SENDVERBS IOCTL to communicate verbs with the audio codec. IOCTL\_AZALIABUS\_SENDVERBS is defined as shown in the following example:

```
#define IOCTL_AZALIABUS_SENDVERBS CTL_CODE(FILE_DEVICE_UNKNOWN, 1, METHOD_BUFFERED, FILE_ANY_ACCESS)
```

For more information about FILE\_DEVICE\_UNKNOWN, METHOD\_BUFFERED, and FILE\_ANY\_ACCESS, see the Devioctl.h header file in the Windows SDK.

To initiate communication with the audio codec, the class driver calls the [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=124239) function with the following parameters.

```
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

If the call to [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) is successful, it returns a nonzero value. If the call fails or is pending (not processed immediately), **DeviceIoControl** returns a zero value. The class driver can call [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) for a more detailed error message.

When the audio driver must change pin configuration defaults, it can use IOCTL\_AZALIABUS\_SENDVERBS to send and receive Set and Get verbs from the audio codec. If communication with the audio codec is not about pin configuration, the audio codec only responds to the Get verb.

The following example shows a function that takes an AzCorbeEntry structure and a HANDLE as parameters and returns the AzRirbResponse from the codec.

```
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

```
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

```
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

```
typedef struct _UserModeCodecCommandPacket
{
  ULONG NumCommands;      // number of commands in this packet
  AzCorbEntry Command[1]; // variable length array of verbs
} UserModeCodecCommandPacket;
```

### <span id="usermodecodecresponsepacket"></span><span id="USERMODECODECRESPONSEPACKET"></span> UserModeCodecResponsePacket

```
typedef struct _UserModeCodecResponsePacket
{
  ULONG NumResponses;       // on successful IOCTL, this will be updated with the number of responses.
  AzRirbEntry Response[1];  // Variable length array of responses. lpOutBuffer param to DeviceIoControl
                            // must point to sufficient space to hold this IOCTL with all its responses 
} UserModeCodecResponsePacket;
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Communicating%20Verbs%20with%20the%20HD%20Audio%20Codec%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


