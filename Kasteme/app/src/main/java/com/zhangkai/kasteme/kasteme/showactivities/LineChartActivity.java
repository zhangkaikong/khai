package com.zhangkai.kasteme.kasteme.showactivities;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.zhangkai.kasteme.kasteme.R;
import com.zhangkai.kasteme.kasteme.customview.LineCharView;

public class LineChartActivity extends AppCompatActivity {
LineCharView mLineChartView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_line_chart);
        mLineChartView = new LineCharView(this);
    }
}
