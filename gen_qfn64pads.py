edge = 9.0/2
rect_size = 0.4+0.4+0.05-0.14
rect_edge = edge + 0.4
rect_center = rect_edge - rect_size/2
circ_center = edge - 0.4 - 0.05 + 0.14
for i in range(0, 16):
  print("""  (pad {} smd rect (at {} {}) (size 0.28 {}) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+1, 0.5*(i-7)-0.25, -rect_center, rect_size))
  print("""  (pad {} smd circle (at {} {}) (size 0.28 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+1, 0.5*(i-7)-0.25, -circ_center))

for i in range(0, 16):
  print("""  (pad {} smd rect (at {} {}) (size {} 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+17, rect_center, 0.5*(i-7)-0.25, rect_size))
  print("""  (pad {} smd circle (at {} {}) (size 0.28 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+17, circ_center, 0.5*(i-7)-0.25))

for i in range(0, 16):
  print("""  (pad {} smd rect (at {} {}) (size 0.28 {}) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+33, -(0.5*(i-7)-0.25), rect_center, rect_size))
  print("""  (pad {} smd circle (at {} {}) (size 0.28 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+33, -(0.5*(i-7)-0.25), circ_center))

for i in range(0, 16):
  print("""  (pad {} smd rect (at {} {}) (size {} 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+49, -rect_center, -(0.5*(i-7)-0.25), rect_size))
  print("""  (pad {} smd circle (at {} {}) (size 0.28 0.28) (layers F.Cu F.Paste F.Mask)
    (solder_mask_margin 0.07))""".
        format(i+49, -circ_center, -(0.5*(i-7)-0.25)))
