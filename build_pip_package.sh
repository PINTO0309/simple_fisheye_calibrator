#!/bin/bash

rm -rf build/
rm -rf dist/
rm -rf simple_fisheye_calibrator.egg-info/
python3 setup.py sdist bdist_wheel