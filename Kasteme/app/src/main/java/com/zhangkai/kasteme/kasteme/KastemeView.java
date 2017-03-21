package com.zhangkai.kasteme.kasteme;

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

        mScreenWidthCenter = mScreenWidth/2;
        mScreenHeightCenter = mScreenHeight/2;
    }

    @Override
    protected void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        Paint p = new Paint();
        p.setColor(Color.BLUE);
        p.setTextSize(28);
        canvas.drawText(mShowText,0, mStatusBarHeight,p);
        if (mX < mScreenWidthCenter) {
            if (mY < mScreenHeightCenter) {
                canvas.drawOval(mX,mY,mScreenWidth - mX,mScreenHeight - mY,p);
            } else {
                canvas.drawOval(mX,mScreenHeight - mY,mScreenWidth - mX,mY,p);
            }
        } else {
            if (mY < mScreenHeightCenter) {
                canvas.drawOval(mScreenWidth - mX,mY,mX,mScreenHeight - mY,p);
            } else {
                canvas.drawOval(mScreenWidth - mX,mScreenHeight - mY,mX,mY,p);
            }
        }
        super.onDraw(canvas);
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        mShowText = ""+event.getAction();
        mX = (int) event.getX();
        mY = (int) event.getY();
//        mShowText += "x=" + mX + ",y=" + mY;
        invalidate();
        return super.onTouchEvent(event);
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
