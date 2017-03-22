package com.zhangkai.kasteme.kasteme.customview;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.util.Log;
import android.view.View;

/**
 * Created by zhangkai on 17-3-22.
 */
public class ScanView extends View {

    private Paint mPaint;
    private static final int MAX_DRAW_TIMES = 360;
    private int mPaintTimes = 0;
    public ScanView(Context context) {
        super(context);
        initialize();
    }

    public ScanView(Context context, AttributeSet attrs) {
        super(context,attrs);
        initialize();
    }

    public void initialize() {
        mPaint = new Paint();
    }
    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        mPaintTimes += 2;
        mPaint.setColor(Color.RED);
        canvas.drawCircle(360,400,190,mPaint);
        mPaint.setColor(Color.GREEN);
        canvas.drawCircle(360,400,185,mPaint);
        mPaint.setColor(Color.BLACK);
        mPaint.setTextSize(25);
        canvas.drawCircle(360,400,5,mPaint);
        canvas.drawText("360装逼卫士",285,160,mPaint);
        canvas.drawText("扫描中,请等待...",280,190,mPaint);

        mPaint.setColor(Color.BLACK);
        mPaint.setAntiAlias(true);
        mPaint.setStrokeWidth(5f);
        int radius = 190;
        int x=0,y=0;
        if (mPaintTimes < 90) {
            x = Math.abs((int)(radius * Math.abs(Math.sin(Math.toRadians(mPaintTimes)))));
            y = Math.abs((int)(radius * Math.abs(Math.cos(Math.toRadians(mPaintTimes)))));
            canvas.drawLine(360,400,360+x,400-y,mPaint);
        } else if (mPaintTimes < 180) {
            x = Math.abs((int)(radius * Math.sin(Math.toRadians(mPaintTimes))));
            y = Math.abs((int)(radius * Math.cos(Math.toRadians(mPaintTimes))));
            canvas.drawLine(360,400,360+x,400+y,mPaint);
        } else if (mPaintTimes < 270) {
            x = Math.abs((int)(radius * Math.sin(Math.toRadians(mPaintTimes))));
            y = Math.abs((int)(radius * Math.cos(Math.toRadians(mPaintTimes))));
            canvas.drawLine(360,400,360-x,400+y,mPaint);
        } else if (mPaintTimes <= 360) {
            x = Math.abs((int)(radius * Math.sin(Math.toRadians(mPaintTimes))));
            y = Math.abs((int)(radius * Math.cos(Math.toRadians(mPaintTimes))));
            canvas.drawLine(360,400,360-x,400-y,mPaint);
        }

        if (mPaintTimes < MAX_DRAW_TIMES) {
            invalidate();
        } else {
            mPaintTimes = 0;
            invalidate();
        }
    }
}
