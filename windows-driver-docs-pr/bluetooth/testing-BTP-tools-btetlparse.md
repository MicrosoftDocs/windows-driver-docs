---
title: Microsoft Bluetooth Test Platform - BTETLParse
description: Bluetooth Test Platform (BTP) Bluetooth ETL parse.
ms.date: 1/12/2021

---
# Bluetooth ETL parse (BTETLParse.exe)

The Bluetooth ETL parse tool extracts HCI traces from ETL files containing compressed Bluetooth data.

This tool is meant for parsing ETL files collected using the [Bus tools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

[Tracefmt](../devtest/tracefmt.md)
is a way to parse additional logs from the ETL file.

## ETL parse command line options

```console
Usage: btetlparse [-cfa <output_cfa_filename>] [-hci <output_hci_filename>]
[-pcap <output_pcap_filename>] [-pcapng <output_pcapng_filename>]
[<input_etl_filename>] [<additional_input_etl_filenames>]

    -cfa through -pcapng flags parse the etl file into different file types.

    -cfa <filename>         Data file readable by Frontline protocol analyzers.

    -hci <filename>         Data file in plain text format.

    -pcap <filename>        Data file readable by Wireshark protocol analyzers.
        
    -pcapng <filename>      Data file readable by Wireshark protocol analyzers.

    <input_etl_filename>    The is the filename of the ETL file we are trying to parse.
                                Default is c:\temp\btetw.etl

    <additional_input_etl_filenames>    BTETLParse can parse multiple ETL files at a time.
```

## ETL parse Usage example

Move the ETL file collected by [Bus tools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md) to the same folder as BTETLParse within the extracted BTP package. Then run:

- `btetlparse -cfa BthTracing.cfa -hci BthTracing.hci -pcap BthTracing.pcap -pcapng BthTracing.pcapng BthTracing.etl` from a command prompt/PowerShell console

This command parses `BthTracing.etl` into all available filetypes. See Command Line Options above for descriptions of each file type.
