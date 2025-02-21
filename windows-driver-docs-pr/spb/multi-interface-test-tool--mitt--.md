---
title: Buy Hardware for Using MITT
description: To you use Multiple Interface Test Tool (MITT), order you need a MITT board and bus-specific adapter boards that plug into ports on the MITT board. The type of adapter board depends on the bus you want to test.
ms.date: 01/12/2024
---

# Buy hardware for using MITT

The Multiple Interface Test Tool (MITT) is a test tool for validating hardware and software for simple peripheral buses, such as UART, I2C, SPI, and GPIO. MITT uses the FPGA development board and includes a software package with firmware, test binaries, and drivers that provide an inexpensive test solution.

To use the Multiple Interface Test Tool (MITT), you need a MITT board and bus-specific adapter boards that plug into ports on the MITT board. The type of adapter board depends on the bus you want to test.

- **MITT board**

    For example, FPGA development board (Nexys A7). See [FPGA board from Digilent](https://digilent.com/reference/programmable-logic/nexys-a7/start).

    :::image type="content" source="images/nexys-a7-top-600.png" alt-text="Picture of a MITT board.":::

- **UART/SPI adapter board**

    See [UART/SPI adapter board from JJG Technologies.](http://www.jjgtechnologies.com/UART-SPI.htm)

    :::image type="content" source="images/uart1.png" alt-text="Picture of a UART adapter board.":::

- **GPIO adapter board**

    See [GPIO adapter board from JJG Technologies.](http://www.jjgtechnologies.com/GPIO.htm)

    :::image type="content" source="images/gpioadapter.jpg" alt-text="Picture of a GPIO adapter for MITT.":::

- **I2C adapter board**

    See [I2C adapter board from JJG Technologies.](http://www.jjgtechnologies.com/I2C.htm)

    :::image type="content" source="images/i2cadapter.jpg" alt-text="Picture of an I2C adapter for MITT.":::

- **MCATT expansion board**

    See [MCATT expansion board from JJG Technologies.](http://www.jjgtechnologies.com/mcatt.htm)

    :::image type="content" source="images/mcatt-exp.jpg" alt-text="Picture of an MCATT expansion board.":::

- **Touch simulator pad**

    Touch simulator pad and a band cable to connect to the adapter. MCATT tool is able to stimulate a capacitive touch device by stimulating the precise points that come in contact with the board. The boards can be customized to have various sized and contact point resolutions.

    :::image type="content" source="images/touch.jpg" alt-text="Picture of a touch simulator pad.":::

    These pad is customized for the device to test.

  - Specific size
  - Number of touch points
  - Distance between the touch points

## Related topics

- [SPI tests in MITT](spi-tests-in-mitt.md)
