package com.zhangkai.kasteme.kasteme.showactivities;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.zhangkai.kasteme.kasteme.R;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemClickListener{

    private ListView mListView;
    private String[] mActivityList = {"柱状图","折线图","扫描","椭圆"};
    private ArrayAdapter mAdapter;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        mListView = (ListView) findViewById(R.id.listView);
        mAdapter = new ArrayAdapter(this,android.R.layout.simple_list_item_1,mActivityList);
        mListView.setAdapter(mAdapter);
        mListView.setOnItemClickListener(this);
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        switch (i) {
            case 0:
                Intent intent1 = new Intent(this,AnimatorActivity.class);
                startActivity(intent1);
                break;
            case 1:
                Intent intent2 = new Intent(this,LineChartActivity.class);
                startActivity(intent2);
                break;
            case 2:
                Intent intent3 = new Intent(this,ScanActivity.class);
                startActivity(intent3);
                break;
            case 3:
                break;
            default:
                break;
        }
    }
}
