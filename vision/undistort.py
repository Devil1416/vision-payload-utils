"""Camera distortion correction using Brown-Conrady model."""
from dataclasses import dataclass
import math

@dataclass
class CameraModel:
    fx: float; fy: float
    cx: float; cy: float
    k1: float = 0.0; k2: float = 0.0
    p1: float = 0.0; p2: float = 0.0

    def undistort_point(self, u: float, v: float) -> tuple[float, float]:
        """Iteratively remove lens distortion from pixel (u, v)."""
        x = (u - self.cx) / self.fx
        y = (v - self.cy) / self.fy
        # 3 iterations of Newton-Raphson
        xd, yd = x, y
        for _ in range(3):
            r2 = xd**2 + yd**2
            radial = 1 + self.k1*r2 + self.k2*r2**2
            xd = (x - 2*self.p1*xd*yd - self.p2*(r2+2*xd**2)) / radial
            yd = (y - self.p1*(r2+2*yd**2) - 2*self.p2*xd*yd) / radial
        return xd * self.fx + self.cx, yd * self.fy + self.cy
