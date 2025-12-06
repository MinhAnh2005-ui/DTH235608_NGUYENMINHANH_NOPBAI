import time

print("Vẽ hình với sleep")

hinh1 = """
       *
       * *
       * * *
 * * * * * * *
 * * *
 * *
 *
"""

hinh2 = """
       *
       * *
       *   *
 * * * * * * *
 *   *
 * *
 *
"""

hinh3 = """
       * * * *
       * * *
       * *
       *
       *
     * *
   * * *
 * * * *
"""

hinh4 = """
       * * * *
       *   *
       * *
       *
       *
     * *
   *   *
 * * * * 
"""

ds_hinh = [hinh1, hinh2, hinh3, hinh4]

for i, h in enumerate(ds_hinh, start=1):
    print(f"\nHình {i}:")
    print(h)
    time.sleep(5)
