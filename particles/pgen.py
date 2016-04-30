#!/usr/bin/python
import sys
import xml.etree.cElementTree as ET

'''
copy and paste from http://effbot.org/zone/element-lib.htm#prettyprint
it basically walks your tree and adds spaces and newlines so the tree is
printed in a nice way
'''
def indent(elem, level=0):
  i = "\n" + level*"  "
  if len(elem):
    if not elem.text or not elem.text.strip():
      elem.text = i + "  "
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
    for elem in elem:
      indent(elem, level+1)
    if not elem.tail or not elem.tail.strip():
      elem.tail = i
  else:
    if level and (not elem.tail or not elem.tail.strip()):
      elem.tail = i

def add_particle(ps, pos, v, r):
  p = ET.SubElement(ps, "particle")
  ET.SubElement(p, "pos").text = str(pos[0])+" "+str(pos[1])+" "+str(pos[2])
  ET.SubElement(p, "v").text = str(v[0])+" "+str(v[1])+" "+str(v[2])
  ET.SubElement(p, "r").text = str(r)

def build_tree():
  particles = ET.Element("particles")
  ps = ET.SubElement(particles, "ps")
  #fs = ET.SubElement(particles, "fs")


  size = 3;
  dis = 0.12;
  r = 0.05

  for i in range(1-size, size):
    for j in range(0,size):
      for k in range(1-size,size):
        add_particle(ps, [dis*i,dis*j+1,dis*k], [0,0,0], r) 
  
  indent(particles)
  return ET.ElementTree(particles)

tree = build_tree()
tree.write("p1.xml")