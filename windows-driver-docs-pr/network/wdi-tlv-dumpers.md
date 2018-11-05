---
title: WDI TLV dumpers
description: The parser generator library has routines to decode TLV byte arrays into trace statements.
ms.assetid: 4F8B53E5-1F51-4119-AC06-7A710340E4A4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI TLV dumpers


The parser generator library has routines to decode TLV byte arrays into trace statements.

```C++
    typedef _Function_class_( TlvDumperCallback ) void( __stdcall *TlvDumperCallback )(_In_ UINT_PTR Context, _In_z_ _Printf_format_string_ PCSTR Format, ...);

    void __stdcall TraceUnknownTlvByteStream(
        _In_ ULONG PeerVersion,
        _In_ ULONG BufferLength,
        _In_reads_bytes_( BufferLength ) UINT8 const * pBuffer );

    void __stdcall TraceMessageTlvByteStream(
        _In_ ULONG MessageId,
        _In_ BOOLEAN fToIhv,
        _In_ ULONG PeerVersion,
        _In_ ULONG BufferLength,
        _In_reads_bytes_( BufferLength ) UINT8 const * pBuffer );

    void __stdcall DumpUnknownTlvByteStream(
        _In_ ULONG PeerVersion,
        _In_ ULONG BufferLength,
        _In_reads_bytes_( BufferLength ) UINT8 const * pBuffer,
        _In_opt_ ULONG_PTR Context,
        _In_opt_ TlvDumperCallback pCallback );

    void __stdcall DumpMessageTlvByteStream(
        _In_ ULONG MessageId,
        _In_ BOOLEAN fToIhv,
        _In_ ULONG PeerVersion,
        _In_ ULONG BufferLength,
        _In_reads_bytes_( BufferLength ) UINT8 const * pBuffer,
        _In_opt_ ULONG_PTR Context,
        _In_opt_ TlvDumperCallback pCallback );
```

If you only need WPP tracing, use the Trace APIs as they are optimized to have the smallest impact to code size as well as log size (fewer strings in the ETL file). If you need a more general purpose dumper, use the Dump APIs as they include WPP tracing and also include a callback routine. The stub driver has an example of using this callback routine to redirect the output to the kernel debugger via DebugPrint APIs.

Unlike the Parse and Generate APIs, the dumper is very permissive. It attempts to make sense of the TLV bytes as best as it can, regardless of the canonical form for a given message or TLV. This means the dumper might correctly decode and dump something that the parser rejects.

**Warning**  If the dumper successfully decodes the bytes into a human readable format, it does not mean the bytes are a well-formed TLV.

 

Like the Parse APIs, the *pBuffer* pointer and *BufferLength* parameters should exclude any headers and point directly at the first TLV.

The Message variants of the APIs include the message ID and the message direction to better disambiguate the TLV. This is helpful because the same TLV ID can be decoded in different ways depending upon context. For example, [**WDI\_TLV\_BSSID**](https://msdn.microsoft.com/library/windows/hardware/dn926153) can directly contain a [**WDI\_MAC\_ADDRESS**](https://msdn.microsoft.com/library/windows/hardware/dn926071) when part of [OID\_WDI\_TASK\_SCAN](https://msdn.microsoft.com/library/windows/hardware/dn925959), or it can contain a list of **WDI\_MAC\_ADDRESS** when part of [**WDI\_TLV\_P2P\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/dn897863).

 

 





