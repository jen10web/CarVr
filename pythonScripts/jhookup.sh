#!/bin/sh

bluetoothctl
power on
agent on
pair 0C:4D:12:11:01:E4
trust 0C:4D:12:11:01:E4
connect 0C:4D:12:11:01:E4
agent off
quit