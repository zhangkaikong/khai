package com.zhangkai.kasteme.kasteme.customview;

import android.content.Context;
import android.content.res.TypedArray;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.WindowManager;

/**
 * Created by zhangkai on 17-3-21.
 */
public class KastemeView extends View {
    int mX,mY = 0;
    private String mShowText = "";
    private int mScreenWidth,mScreenHeight;
    private int mScreenWidthCenter,mScreenHeightCenter;
    private int mActionBarHeight;
    private int mStatusBarHeight;
    private static final int TOTAL_PAINT_TIMES = 100;
    private int mPaintTimes = 0;
    private Paint mPaint;

    public KastemeView(Context context){
       super(context);
    }

    public KastemeView(Context context, AttributeSet attrs){
        super(context,attrs);
        TypedArray actionbarSizeTypedArray = context.obtainStyledAttributes(new int[] { android.R.attr.actionBarSize});
        float h = actionbarSizeTypedArray.getDimension(0, 0);
        mActionBarHeight = (int)h;
        mStatusBarHeight = getStatusBarHeight(context);

        DisplayMetrics metrics = new DisplayMetrics();
        WindowManager wms = (WindowManager)context.getSystemService(Context.WINDOW_SERVICE);
        wms.getDefaultDisplay().getMetrics(metrics);
        mScreenWidth = (int)metrics.widthPixels;
        mScreenHeight = (int)metrics.heightPixels - mActionBarHeight - mStatusBarHeight;

        mPaint = new Paint();
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        mPaintTimes++;
        mPaint.setColor(Color.BLUE);
        mPaint.setTextSize(28);
        canvas.drawText(mShowText,0, mStatusBarHeight,mPaint);
        int screenWidth = mScreenWidth/TOTAL_PAINT_TIMES*mPaintTimes;
        int screenHeight = mScreenHeight/TOTAL_PAINT_TIMES*mPaintTimes;

        mScreenWidthCenter = screenWidth/2;
        mScreenHeightCenter = screenHeight/2;

        canvas.drawOval(0,0,screenWidth,screenHeight,mPaint);

        if (mPaintTimes < TOTAL_PAINT_TIMES) {
            invalidate();
        }
    }

    public static int getStatusBarHeight(Context context) {
        Class<?> c = null;
        Object obj = null;
        java.lang.reflect.Field field = null;
        int x = 0;
        int statusBarHeight = 0;
        try {
            c = Class.forName("com.android.internal.R$dimen");
            obj = c.newInstance();
            field = c.getField("status_bar_height");
            x = Integer.parseInt(field.get(obj).toString());
            statusBarHeight = context.getResources().getDimensionPixelSize(x);
            return statusBarHeight;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return statusBarHeight;
    }
}
