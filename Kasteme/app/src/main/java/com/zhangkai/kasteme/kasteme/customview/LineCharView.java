package com.zhangkai.kasteme.kasteme.customview;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.View;

/**
 * Created by zhangkai on 17-3-21.
 */
public class LineCharView extends View {

    private Paint mPaint;
    private int[][] mCordinates = {{70,450},{130,250},{190,190},{250,400},{310,60},{370,110},{430,300},{490,70},{550,250},{610,20},{670,550}};
    private static final int MAX_DRAW_TIMES = 11;
    private int mDrawTimes = 0;

    public LineCharView(Context context){
        super(context);
        initialize();
    }

    public LineCharView(Context context, AttributeSet attrs){
        super(context,attrs);
        initialize();
    }

    public void initialize(){
        mPaint = new Paint();
        mPaint.setAntiAlias(true);
        mPaint.setStrokeWidth(5f);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        mDrawTimes++;
        mPaint.setColor(Color.BLACK);
        canvas.drawLine(70,50,70,650,mPaint);
        canvas.drawLine(70,650,690,650,mPaint);
        mPaint.setColor(Color.RED);
        canvas.drawLine(70,550,690,550,mPaint);
        canvas.drawLine(70,450,690,450,mPaint);
        canvas.drawLine(70,350,690,350,mPaint);
        canvas.drawLine(70,250,690,250,mPaint);
        canvas.drawLine(70,150,690,150,mPaint);
        mPaint.setColor(Color.BLACK);
        canvas.drawText(String.valueOf(150),30,550,mPaint);
        canvas.drawText(String.valueOf(250),30,450,mPaint);
        canvas.drawText(String.valueOf(350),30,350,mPaint);
        canvas.drawText(String.valueOf(450),30,250,mPaint);
        canvas.drawText(String.valueOf(550),30,150,mPaint);
        for (int i = 0;i < mDrawTimes;i++) {
            mPaint.setColor(Color.BLACK);
            if (i == mDrawTimes - 1) {
                canvas.drawText(String.valueOf(mCordinates[i][0]),mCordinates[i][0]-15,680,mPaint);
                mPaint.setColor(Color.BLUE);
                canvas.drawText(String.valueOf(mCordinates[i][1]),mCordinates[i][0],mCordinates[i][1],mPaint);
            } else {
                canvas.drawText(i==0?String.valueOf(0):String.valueOf(mCordinates[i-1][0]),mCordinates[i][0]-10,680,mPaint);
                mPaint.setColor(Color.BLUE);
                canvas.drawLine(mCordinates[i][0],mCordinates[i][1],mCordinates[i+1][0],mCordinates[i+1][1],mPaint);
                canvas.drawText(String.valueOf(mCordinates[i][1]),mCordinates[i][0],mCordinates[i][1],mPaint);
            }

        }
        try {
            Thread.sleep(100);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        if (mDrawTimes < MAX_DRAW_TIMES) {
            invalidate();
        } else {
            mDrawTimes = 0;
            invalidate();
        }
    }
}
